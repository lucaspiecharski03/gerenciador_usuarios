from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[DataRequired()])
    real_name = StringField('Nome Real', validators=[DataRequired()])
    is_active = BooleanField('Ativo')
    submit = SubmitField('Registar-se')
