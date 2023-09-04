from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.registration_form import RegistrationForm

register_blueprint = Blueprint('register', __name__, url_prefix='/register')


@register_blueprint.route('/register', methods=["GET"])
def register_get():
    registration_form = RegistrationForm()
    return render_template('auth/register.html', form=registration_form)