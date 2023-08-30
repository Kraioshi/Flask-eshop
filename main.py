from flask import Flask, render_template
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
    return render_template('index.html')


@app.route('/register')
def register():
    pass


@app.route('/login')
def login():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/add_product')
def add_product():
    add_product_form = AddProductForm()
    return render_template('add_product.html', form=add_product_form)


if __name__ == "__main__":
    app.run(debug=True)
