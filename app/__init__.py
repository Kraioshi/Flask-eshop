from flask import Flask, Blueprint
from flask_mail import Mail, Message
from flask_login import login_user, LoginManager, current_user, logout_user, login_required

from app.models import db
from app.models.user import User
from app.config import Config
# from app.routes.auth.test import test_blueprint


def create_app():
    app = Flask(__name__)

    # TODO: register blueprints here
    # app.register_blueprint(test_blueprint)

    # Configuration
    app.config.from_object(Config)

    mail = Mail(app)
    db.init_app(app)

    # Initialize the LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login_get'

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)

    # Initialize database
    with app.app_context():
        db.create_all()

    return app
