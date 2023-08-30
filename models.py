from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    quantity = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
