from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

from app.models import db
from app.models.models import Product

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    result = db.session.execute(db.Select(Product))
    all_products = result.scalars().all()
    return render_template('index.html', products=all_products, current_user=current_user)