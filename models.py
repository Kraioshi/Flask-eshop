from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)

    wished = relationship("Wishlist", back_populates='product')


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    wishes = relationship("Wishlist", back_populates='owner')


class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = relationship("User", back_populates='wishes')

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = relationship("Product", back_populates='wished')

    product_title = db.Column(db.String(250), db.ForeignKey('products.title'))
    product_image = db.Column(db.LargeBinary, db.ForeignKey('products.image_data'))



