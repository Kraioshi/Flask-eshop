from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db
from app.models.models import Product

add_to_cart_bp = Blueprint('add_to_cart', __name__)


@add_to_cart_bp.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    requested_product = db.get_or_404(Product, product_id)

    if requested_product not in current_user.cart:
        current_user.cart.append(requested_product)
        db.session.commit()
        return redirect(url_for('cart.cart'))
    else:
        flash("You have already added this product to your cart")

    return redirect(url_for('login.login_get'))
