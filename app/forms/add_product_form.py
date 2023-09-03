from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, DecimalField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    title = StringField("Product Name", validators=[DataRequired()],
                        render_kw={'placeholder': 'Title'})
    subtitle = StringField("Short Description", validators=[DataRequired()],
                           render_kw={'placeholder': 'Short Description'})
    description = TextAreaField("Product Description", validators=[DataRequired()],
                                render_kw={"style": "height: 120px;",
                                           'placeholder': 'Product Description'})
    price = DecimalField("Price", validators=[DataRequired()],
                         render_kw={'placeholder': 'Price'})
    quantity = IntegerField("Quantity", validators=[DataRequired()],
                            render_kw={'placeholder': 'Quantity'})
    image = StringField("Image Path", validators=[DataRequired()],
                        render_kw={'placeholder': 'Image Path'})
    submit = SubmitField("Add Product",
                         render_kw={'class': 'add-product-submit'})
