from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from models import db, Product
from forms import AddProductForm

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config["SECRET_KEY"] = 'verysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shop.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    result = db.session.execute(db.Select(Product))
    all_products = result.scalars().all()
    return render_template('index.html', products=all_products)


@app.route('/register')
def register():
    pass


@app.route('/login')
def login():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/add_product', methods=["GET"])
def add_product_get():
    add_product_form = AddProductForm()
    return render_template('add_product.html', form=add_product_form)


@app.route('/add_product', methods=["POST"])
def add_product_post():
    add_product_form = AddProductForm()
    if add_product_form.validate_on_submit():
        new_product = Product(
            title=add_product_form.title.data,
            subtitle=add_product_form.subtitle.data,
            description=add_product_form.description.data,
            price=add_product_form.price.data,
            quantity=add_product_form.quantity.data,
            img_url=add_product_form.img_url.data
        )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/products/<int:product_id>', methods=["GET"])
def product_get(product_id):
    requested_product = db.get_or_404(Product, product_id)
    return render_template('product.html', product=requested_product)


if __name__ == "__main__":
    app.run(debug=True)
