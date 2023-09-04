from flask import Blueprint, render_template, redirect, url_for

from app.forms.add_product_form import AddProductForm
from admin import admin_only

from app.models import db
from app.models.models import Product

add_product_bp = Blueprint("add_product", __name__)


@add_product_bp.route('/add_product', methods=["GET"])
@admin_only
def add_product_get():
    add_product_form = AddProductForm()
    return render_template('products/add_product.html', form=add_product_form)


@add_product_bp.route('/add_product', methods=["POST"])
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
