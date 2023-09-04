from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.forms.login_form import Loginform
from app.models import db
from app.models.models import User


login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=["GET"])
def login_get():
    login_form = Loginform()
    return render_template("auth/login.html", form=login_form)


@login_bp.route('/login', methods=["POST"])
def login_post():
    login_form = Loginform()
    if login_form.validate_on_submit():
        password = login_form.password.data
        result = db.session.execute(db.Select(User).where(User.email == login_form.email.data))
        existing_user = result.scalar()

        if not existing_user or not check_password_hash(existing_user.password, password):
            flash("Incorrect email or password. Please try again")
            return redirect(url_for('login_get'))

        else:
            login_user(existing_user)
            return redirect(url_for('index'))
