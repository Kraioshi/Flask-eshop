from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    message = TextAreaField("Your Message", validators=[DataRequired()],
                            render_kw={"style": "height: 120px;",
                                       'placeholder': 'Your Message'})

    submit = SubmitField("Send Email", render_kw={'class': 'send-email-submit'})
