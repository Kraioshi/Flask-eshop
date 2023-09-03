from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap5
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, Product, User
from forms import AddProductForm, RegistrationForm, Loginform
from admin import admin_only

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config["SECRET_KEY"] = 'verysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shop.db"
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_get'


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    result = db.session.execute(db.Select(Product))
    all_products = result.scalars().all()
    return render_template('index.html', products=all_products, current_user=current_user)


@app.route('/register', methods=["GET"])
def register_get():
    registration_form = RegistrationForm()
    return render_template('auth/register.html', form=registration_form)


@app.route('/register', methods=["POST"])
def register_post():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():

        result = db.session.execute(db.Select(User).where(User.email == registration_form.email.data))
        existing_user = result.scalar()

        if existing_user:
            flash("Email already registered! Try new email or log in instead!")
            return redirect(url_for('register_get'))

        hashed_password = generate_password_hash(
            registration_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name=registration_form.name.data,
            email=registration_form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('index'))


@app.route('/login', methods=["GET"])
def login_get():
    login_form = Loginform()
    return render_template("auth/login.html", form=login_form)


@app.route('/login', methods=["POST"])
def login_post():
    login_form = Loginform()
    if login_form.validate_on_submit():
        password = login_form.password.data
        result = db.session.execute(db.Select(User).where(User.email == login_form.email.data))
        existing_user = result.scalar()

        if not existing_user or not check_password_hash(existing_user.password, password):
            flash("Incorrect email or password. Please try again")
            return redirect(url_for('login_get'))

        else:
            login_user(existing_user)
            return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/add_product', methods=["GET"])
@admin_only
def add_product_get():
    add_product_form = AddProductForm()
    return render_template('products/add_product.html', form=add_product_form)


@app.route('/add_product', methods=["POST"])
@admin_only
def add_product_post():
    add_product_form = AddProductForm()
    if add_product_form.validate_on_submit():
        new_product = Product(
            title=add_product_form.title.data,
            subtitle=add_product_form.subtitle.data,
            description=add_product_form.description.data,
            price=add_product_form.price.data,
            quantity=add_product_form.quantity.data,
            image_path=add_product_form.image.data
        )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/products/<int:product_id>', methods=["GET"])
def product_get(product_id):
    requested_product = db.get_or_404(Product, product_id)
    return render_template('products/product.html', product=requested_product)


@app.route('/user')
def user():
    return render_template('user/user.html')


@app.route('/cart')
def cart():
    user_cart = current_user.cart
    return render_template('user/cart.html', cart_products=user_cart)


@app.route('/wishlist')
def wishlist():
    user_wishlist = current_user.wishlist
    return render_template('user/wishlist.html', wishlist_products=user_wishlist)


@app.route('/add_to_wishlist/<int:product_id>')
@login_required
def add_to_wishlist(product_id):
    requested_product = db.get_or_404(Product, product_id)

    if requested_product not in current_user.wishlist:
        current_user.wishlist.append(requested_product)
        db.session.commit()
        return redirect(url_for('wishlist'))
    else:
        flash("You have already added this product to your wishlist")

    return redirect(url_for('login_get'))


@app.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    requested_product = db.get_or_404(Product, product_id)

    if requested_product not in current_user.cart:
        current_user.cart.append(requested_product)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        flash("You have already added this product to your cart")

    return redirect(url_for('login_get'))


@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/delete_from_cart/<int:product_id>")
def delete_from_cart(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    if product_to_delete in current_user.cart:
        current_user.cart.remove(product_to_delete)
        db.session.commit()

    return redirect(url_for('cart'))


@app.route('/delete_from_wishlist/<int:product_id>')
def delete_from_wishlist(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    if product_to_delete in current_user.wishlist:
        current_user.wishlist.remove(product_to_delete)
        db.session.commit()

    return redirect(url_for('wishlist'))


@app.route('/images/<int:image_id>')
def get_image(image_id):
    image = Product.query.get(image_id)
    return app.response_class(image.image_data, content_type='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)
