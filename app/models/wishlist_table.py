from sqlalchemy.dialects.mysql import INTEGER
from models import db

wishlist_table = db.Table(
    'wishlist_table',
    db.Column('user_id', INTEGER(unsigned=True), db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id', INTEGER(unsigned=True), db.ForeignKey('product.id'), primary_key=True)
)