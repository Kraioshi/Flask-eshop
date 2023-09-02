from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

db = SQLAlchemy()

wishlist_table = db.Table(
    'wishlist_table',
    db.Column('user_id', INTEGER(unsigned=True), db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id', INTEGER(unsigned=True), db.ForeignKey('product.id'), primary_key=True)
)

cart_table = db.Table(
    'cart_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    wishlist = relationship('Product', secondary=wishlist_table, back_populates='wishlist_user')
    cart = relationship('Product', secondary=cart_table, back_populates='cart_user')


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
