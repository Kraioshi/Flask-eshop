from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

wishlist_table = db.Table(
    'wishlist_table',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True, ),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)

cart_table = db.Table(
    'cart_table',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    wishlist = relationship('Product', secondary=wishlist_table, back_populates='wishlist_user')
    cart = relationship('Product', secondary=cart_table, back_populates='cart_user')


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)

    wishlist_user = relationship('User', secondary=wishlist_table, back_populates='wishlist')
    cart_user = relationship('User', secondary=cart_table, back_populates='cart')
