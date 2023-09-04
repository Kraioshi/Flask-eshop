from flask import Blueprint, render_template
from app.forms.contact_form import ContactForm

contact_bp = Blueprint('contact', __name__)


@contact_bp.route("/contact", methods=["GET"])
def contact_get():
    contact_form = ContactForm()
    return render_template('contact.html', form=contact_form)