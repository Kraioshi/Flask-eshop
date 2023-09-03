from models import db
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from wishlist_table import wishlist_table
from cart_table import cart_table


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.DECIMAL(precision=10, scale=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)

    wishlist_user = relationship('User', secondary=wishlist_table, back_populates='wishlist')
    cart_user = relationship('User', secondary=cart_table, back_populates='cart')
