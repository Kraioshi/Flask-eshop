from flask import Blueprint, redirect, url_for
from flask_login import current_user
from app.models import db
from app.models.models import Product

delete_from_cart_bp = Blueprint('delete_from_cart', __name__)


@delete_from_cart_bp.route("/delete_from_cart/<int:product_id>")
def delete_from_cart(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    if product_to_delete in current_user.cart:
        current_user.cart.remove(product_to_delete)
        db.session.commit()

    return redirect(url_for('cart.cart'))