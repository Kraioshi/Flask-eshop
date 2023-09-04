from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user

from app.forms.registration_form import RegistrationForm
from werkzeug.security import generate_password_hash

from app.models import db
from app.models.models import User


register_bp = Blueprint('register', __name__)


@register_bp.route('/register', methods=["GET"])
def register_get():
    registration_form = RegistrationForm()
    return render_template('auth/register.html', form=registration_form)


@register_bp.route('/register', methods=["POST"])
def register_post():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():

        result = db.session.execute(db.Select(User).where(User.email == registration_form.email.data))
        existing_user = result.scalar()

        if existing_user:
            flash("Email already registered! Try new email or log in instead!")
            return redirect(url_for('register_get'))

        hashed_password = generate_password_hash(
            registration_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name=registration_form.name.data,
            email=registration_form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('index'))
