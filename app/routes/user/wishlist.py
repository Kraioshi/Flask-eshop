from flask import Blueprint, render_template
from flask_login import current_user

wishlist_bp = Blueprint('wishlist', __name__)


@wishlist_bp.route('/wishlist')
def wishlist():
    user_wishlist = current_user.wishlist
    return render_template('user/wishlist.html', wishlist_products=user_wishlist)
