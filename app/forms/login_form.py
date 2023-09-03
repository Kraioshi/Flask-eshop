from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Length, EqualTo, InputRequired


class Loginform(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()],
                       render_kw={'placeholder': 'Email',
                                  'class': 'login-email'})

    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, message='Too short')],
                             render_kw={'placeholder': 'Password',
                                        'class': 'login-password'})

    submit = SubmitField("Sign Up", render_kw={'class': 'login-submit'})
