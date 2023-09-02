from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, \
    IntegerField, TextAreaField, EmailField, FileField
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
    image = StringField("Image Path", validators=[DataRequired()],
                        render_kw={'placeholder': 'Image Path'})
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


class Loginform(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()],
                       render_kw={'placeholder': 'Email',
                                  'class': 'login-email'})

    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, message='Too short')],
                             render_kw={'placeholder': 'Password',
                                        'class': 'login-password'})

    submit = SubmitField("Sign Up", render_kw={'class': 'login-submit'})
