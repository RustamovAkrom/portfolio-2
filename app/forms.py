from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login", validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError("User not found !")


class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=150)])
    email = EmailField("Email", validators=[DataRequired(), ])
    password = PasswordField("Password", validators=[DataRequired(), ])
    cofirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    
    def validate_usernaname(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username already taken. Pleace chooce another one")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That Email already taken. Please choose another one")
