from flask import Blueprint, redirect, url_for, flash, current_app
from flask_login import current_user
from flask_mail import Message
import os

from app.forms.contact_form import ContactForm

send_email_bp = Blueprint('send_email', __name__)


@send_email_bp.route('/contact', methods=["POST"])
def send_email():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        sender_name = current_user.name
        sender_email = current_user.email
        sender_message = contact_form.message.data

        message_body = f"New Message From {sender_email}\n\n" \
                       f"{sender_message}"

        message = Message(subject=f"New message from {sender_name}",
                          sender=os.getenv("MAIL_USERNAME"),
                          recipients=[os.getenv("MAIL_USERNAME")],
                          body=message_body)

        mail = current_app.extensions.get('mail')
        mail.send(message)

        flash("Your message has been sent successfully!")
        return redirect(url_for('redirect.redirect_home'))
