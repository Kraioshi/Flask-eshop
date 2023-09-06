from flask import Blueprint, render_template
from flask_login import current_user

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/cart')
def cart():
    user_cart = current_user.cart
    return render_template('user/cart.html', cart_products=user_cart)
