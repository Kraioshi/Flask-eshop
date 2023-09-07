from flask import Blueprint, request, url_for, redirect
import stripe
from stripe import Customer, Charge

public_key =
stripe.api_key =

payment_bp = Blueprint('payment', __name__)


@payment_bp.route('/payment', methods=["POST"])
def payment():
    # CUSTOMER INFORMATION
    customer = Customer.create(email=request.form['stripeEmail'],
                               source=request.form['stripeToken'])

    #PAYMENT
    charge = Charge.create(
        customer=customer.id,
        amount=1999,
        current='usd',
        description='The Description Here',

    )

    return redirect(url_for('index.index'))