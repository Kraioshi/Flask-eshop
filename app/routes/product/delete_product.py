from flask import Blueprint, redirect, url_for

from app.models import db
from app.models.models import Product

delete_product_bp = Blueprint('delete_product', __name__)


@delete_product_bp.route('/delete/<int:product_id>')
def delete_product(product_id):
    product_to_delete = db.get_or_404(Product, product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect(url_for('index.index'))