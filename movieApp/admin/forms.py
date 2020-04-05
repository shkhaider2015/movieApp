from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField,
                     SelectMultipleField)
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, file_allowed
from wtforms.fields.html5 import DateField


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login as admin")


class DataSubmitForm(FlaskForm):
    movie_title = StringField("Title", validators=[DataRequired()])
    movie_industry = StringField("Industry", validators=[DataRequired()])
    movie_genr = StringField("Genr", validators=[DataRequired()])
    movie_image = FileField("upload Picture", validators=[file_allowed(['jpg', 'png'])])
    release_date = DateField("DatePicker", format="%Y-%m-%d")
    # cast = SelectMultipleField("Select Cast", choices=[''])
    submit = SubmitField("Add")
