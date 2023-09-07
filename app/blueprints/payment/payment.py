from flask import Blueprint, request, url_for, redirect
from flask_login import current_user
import stripe
from stripe import Customer, Charge

public_key = 'pk_test_51NnnjGCKKdvgdbMlhv3RFUkMBwSKj1wArUrXhIPBEaLMH6UHwYlKePmipB4plarS5A7pYjTo24DKWTUXutEQdXNo00jAdYi28v'
stripe.api_key = 'sk_test_51NnnjGCKKdvgdbMlVHrzh80PDBQY9Fg4FS815OlTzUAKclhDktv7XNaGoBE0tZWetX55tEfFrAnmxPdGEFThjv9M00BdMyO9Lc'

payment_bp = Blueprint('payment', __name__)


@payment_bp.route('/payment', methods=["POST"])
def payment():
    user_cart = current_user.cart
    # CUSTOMER INFORMATION
    customer = Customer.create(email=request.form['stripeEmail'],
                               source=request.form['stripeToken'])

    #PAYMENT
    charge = Charge.create(
        customer=customer.id,
        amount=user_cart.price,
        currency='usd',
        description='The Description Here',

    )

    return redirect(url_for('index.index'))