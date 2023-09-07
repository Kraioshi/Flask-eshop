from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

from app.models import db
from app.models.models import User, Product, wishlist_table, cart_table
from config import Config

from app.blueprints.auth.login import login_bp
from app.blueprints.auth.register import register_bp
from app.blueprints.auth.logout import logout_bp

from app.blueprints.index.index import index_bp

from app.blueprints.product.add_product import add_product_bp
from app.blueprints.product.get_product import get_product_bp
from app.blueprints.product.delete_product import delete_product_bp

from app.blueprints.user.user import user_bp
from app.blueprints.user.cart import cart_bp
from app.blueprints.user.wishlist import wishlist_bp
from app.blueprints.user.add_to_cart import add_to_cart_bp
from app.blueprints.user.delete_from_cart import delete_from_cart_bp
from app.blueprints.user.add_to_wishlist import add_to_wish_bp
from app.blueprints.user.delete_from_wishlist import delete_from_wish_bp

from app.blueprints.contact.contact_get import contact_bp
from app.blueprints.contact.send_email import send_email_bp

from app.blueprints.payment.checkout import checkout_bp
from app.blueprints.payment.payment import payment_bp

from app.blueprints.redirect.redirect_home import redirect_bp

def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates')

    # Load configuration
    app.config.from_object(Config)

    # Load database
    db.init_app(app)

    # Blueprint registration
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logout_bp)

    app.register_blueprint(index_bp)

    app.register_blueprint(add_product_bp)
    app.register_blueprint(get_product_bp)
    app.register_blueprint(delete_product_bp)

    app.register_blueprint(user_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(wishlist_bp)
    app.register_blueprint(add_to_cart_bp)
    app.register_blueprint(add_to_wish_bp)
    app.register_blueprint(delete_from_cart_bp)
    app.register_blueprint(delete_from_wish_bp)

    app.register_blueprint(contact_bp)
    app.register_blueprint(send_email_bp)

    app.register_blueprint(checkout_bp)

    app.register_blueprint(payment_bp)

    app.register_blueprint(redirect_bp)

    # Initialize the LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.login_get'

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)

    # Initialize database
    with app.app_context():
        db.create_all()

    # Bootstrap
    bootstrap = Bootstrap5(app)

    mail = Mail(app)

    return app
