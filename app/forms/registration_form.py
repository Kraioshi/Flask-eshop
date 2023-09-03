from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField,
from wtforms.validators import DataRequired, Length, InputRequired

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
