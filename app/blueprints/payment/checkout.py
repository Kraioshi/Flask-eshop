from flask import Blueprint, render_template
from flask_login import login_required
import stripe

public_key =
stripe.api_key =


checkout_bp = Blueprint('checkout', __name__)


@checkout_bp.route('/checkout', methods=["GET"])
@login_required
def checkout_get():
    return render_template('payment/checkout.html', public_key=public_key)

