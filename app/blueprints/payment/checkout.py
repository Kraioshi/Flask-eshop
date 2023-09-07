from flask import Blueprint, render_template
from flask_login import login_required, current_user
import stripe
from dotenv import load_dotenv
import os

load_dotenv()

public_key = os.getenv("STRIPE_PUBLIC")
stripe.api_key = os.getenv("STRIPE_SECRET")

checkout_bp = Blueprint('checkout', __name__)


@checkout_bp.route('/checkout', methods=["GET"])
@login_required
def checkout_get():
    total_price = sum(item.price for item in current_user.cart)

    return render_template('payment/checkout.html', public_key=public_key, total_price=total_price)


