from flask import Blueprint, render_template

from app.models import db
from app.models.models import Product

get_product_bp = Blueprint("get_product", __name__)


@get_product_bp.route('/products/<int:product_id>', methods=["GET"])
def product_get(product_id):
    requested_product = db.get_or_404(Product, product_id)
    return render_template('products/product.html', product=requested_product)