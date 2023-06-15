from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import HiddenInput

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DeleteUserForm(FlaskForm):
    user_id = StringField('User ID', widget=HiddenInput())
    submit = SubmitField('Hapus')