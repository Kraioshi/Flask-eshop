from flask import Blueprint, request, url_for, redirect
from flask_login import current_user
import stripe
from stripe import Customer, Charge
from dotenv import load_dotenv
import os

load_dotenv()

public_key = os.getenv("STRIPE_PUBLIC")
stripe.api_key = os.getenv("STRIPE_SECRET")

payment_bp = Blueprint('payment', __name__)


@payment_bp.route('/payment', methods=["POST"])
def payment():
    total_price = sum(item.price for item in current_user.cart)

    # CUSTOMER INFORMATION
    customer = Customer.create(email=request.form['stripeEmail'],
                               source=request.form['stripeToken'])

    #PAYMENT
    charge = Charge.create(
        customer=customer.id,
        amount=int(total_price * 100),
        currency='usd',
        description='The Description Here',

    )

    return redirect(url_for('index.index', total_price=total_price))
