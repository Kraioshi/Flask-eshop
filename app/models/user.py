from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from models import db
from wishlist_table import wishlist_table


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    wishlist = relationship('Product', secondary=wishlist_table, back_populates='wishlist_user')
    cart = relationship('Product', secondary=cart_table, back_populates='cart_user')
