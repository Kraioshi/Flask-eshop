from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db
from app.models.models import Product

add_to_wish_bp = Blueprint('add_to_wishlist', __name__)


@add_to_wish_bp.route('/add_to_wishlist/<int:product_id>')
@login_required
def add_to_wishlist(product_id):
    requested_product = db.get_or_404(Product, product_id)

    if requested_product not in current_user.wishlist:
        current_user.wishlist.append(requested_product)
        db.session.commit()
        return redirect(url_for('wishlist.wishlist'))
    else:
        flash("You have already added this product to your wishlist")
        return redirect(url_for('index.index'))
