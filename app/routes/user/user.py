from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def user():
    return render_template('user/user.html')