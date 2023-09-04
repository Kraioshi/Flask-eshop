from flask import Blueprint
from app.routes.auth import login, register, logout

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.register_blueprint(login.login_blueprint)
auth_blueprint.register_blueprint(register.register_blueprint)
auth_blueprint.register_blueprint(logout.logout_blueprint)
