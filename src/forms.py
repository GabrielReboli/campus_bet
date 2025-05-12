from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, DateField, DecimalField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, Regexp, ValidationError
import datetime
import sqlalchemy as sa
from src import db
from src.models import User

# Mock para validação de email único (numa app real, consultaria a BD)
from .mock_data import get_user_by_email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_data_nascimento(self, data_nascimento):
        if data_nascimento.data > datetime.date.today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        # Pode adicionar validação de idade mínima aqui se necessário

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ProfileEditForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=2, max=50)])
    sobrenome = StringField("Sobrenome", validators=[DataRequired(), Length(min=2, max=50)])
    universidade = StringField("Universidade", validators=[DataRequired(), Length(min=3, max=100)])
    about_me = TextAreaField("Sobre mim", validators=[Optional(), Length(max=500)])
    # Campos para mudança de senha (opcional)
    current_password = PasswordField("Senha Atual (deixe em branco se não quiser mudar)")
    new_password = PasswordField("Nova Senha")
    confirm_new_password = PasswordField("Confirmar Nova Senha", validators=[EqualTo("new_password", message="As novas senhas devem coincidir.")])
    submit = SubmitField("Salvar Alterações")

class BetSubmissionForm(FlaskForm):
    # Este formulário seria mais dinâmico numa aplicação real, populado com odds do evento
    # Para mock, podemos simplificar
    amount_staked = DecimalField("Valor da Aposta", validators=[DataRequired()], places=2)
    # Exemplo de seleção de odd (numa app real, viria do evento)
    selected_odd_id = SelectField("Escolha a Odd", coerce=int, validators=[DataRequired()]) 
    submit = SubmitField("Fazer Aposta")

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


