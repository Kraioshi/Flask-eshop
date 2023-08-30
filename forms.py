from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


class AddProductForm(FlaskForm):
    title = StringField("Product Name", validators=[DataRequired()])
    subtitle = StringField("Short Description", validators=[DataRequired()])
    description = StringField("Product Description", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Add Product")
