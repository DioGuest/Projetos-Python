from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
