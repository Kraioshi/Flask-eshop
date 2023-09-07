from flask import Blueprint, render_template
from flask_login import login_required, current_user
import stripe

public_key = 'pk_test_51NnnjGCKKdvgdbMlhv3RFUkMBwSKj1wArUrXhIPBEaLMH6UHwYlKePmipB4plarS5A7pYjTo24DKWTUXutEQdXNo00jAdYi28v'
stripe.api_key = 'sk_test_51NnnjGCKKdvgdbMlVHrzh80PDBQY9Fg4FS815OlTzUAKclhDktv7XNaGoBE0tZWetX55tEfFrAnmxPdGEFThjv9M00BdMyO9Lc'


checkout_bp = Blueprint('checkout', __name__)


@checkout_bp.route('/checkout', methods=["GET"])
@login_required
def checkout_get():
    user_cart = current_user.cart
    return render_template('payment/checkout.html', public_key=public_key, cart_products=user_cart)


