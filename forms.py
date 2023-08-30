from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, IntegerField, TextAreaField, EmailField
from wtforms.validators import DataRequired, URL, Length, EqualTo, InputRequired


class AddProductForm(FlaskForm):
    title = StringField("Product Name", validators=[DataRequired()],
                        render_kw={'placeholder': 'Title'})
    subtitle = StringField("Short Description", validators=[DataRequired()],
                           render_kw={'placeholder': 'Short Description'})
    description = TextAreaField("Product Description", validators=[DataRequired()],
                                render_kw={"style": "height: 120px;",
                                           'placeholder': 'Product Description'})
    price = FloatField("Price", validators=[DataRequired()],
                       render_kw={'placeholder': 'Price'})
    quantity = IntegerField("Quantity", validators=[DataRequired()],
                            render_kw={'placeholder': 'Quantity'})
    img_url = StringField("Product Image URL", validators=[DataRequired(), URL()],
                          render_kw={'placeholder': 'Product Image URL'})
    submit = SubmitField("Add Product",
                         render_kw={'class': 'add-product-submit'})


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()],
                       render_kw={'placeholder': 'Name',
                                  'class': 'register-name'})

    email = EmailField("Email", validators=[DataRequired()],
                       render_kw={'placeholder': 'Email',
                                  'class': 'register-email'})

    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, message='Too short')],
                             render_kw={'placeholder': 'Password',
                                        'class': 'register-password'})

    submit = SubmitField("Sign Up", render_kw={'class': 'register-submit'})
