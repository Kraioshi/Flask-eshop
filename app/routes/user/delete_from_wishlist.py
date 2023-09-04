from flask import Blueprint, redirect, url_for
from flask_login import current_user
from app.models import db
from app.models.models import Product

delete_from_wish_bp = Blueprint('delete_from_wishlist', __name__)


@delete_from_wish_bp.route('/delete_from_wishlist/<int:product_id>')
def delete_from_wishlist(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    if product_to_delete in current_user.wishlist:
        current_user.wishlist.remove(product_to_delete)
        db.session.commit()

    return redirect(url_for('wishlist.wishlist'))