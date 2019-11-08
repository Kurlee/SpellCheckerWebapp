from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email
from SpellCheckApp.models import User

"""
 2FA field will be populated by a valid phone number requested with a specific format
 Phone number formats accepted will be:
 (XXX)-XXX-XXXX
 XXX-XXX-XXXX
 XXXXXXXXXX
 Number will be sanitized to a ten digit, string and checked for the following requirements
 Sanitized number must contain exactly 10 digits (no country codes)
 Sanitized number must contain only digits
 The only allowed formatting chars are (, ), and -
"""


def validate_phone(form, field):
    # form is the registration form below
    # field is the phone number passed as two_fa
    if len(field.data) > 14:
        raise ValidationError('Failure: This is an invalid phone number, too many characters')
    else:
        sanitized_phone_number = field.data.strip(' ()-')
        if len(sanitized_phone_number) == 10 or len(sanitized_phone_number) == 11:
            for i in range(len(sanitized_phone_number)):
                if sanitized_phone_number[i].isnumeric():
                    continue
                else:
                    raise ValidationError('Failure: Phone numbers must only contain numbers')
        else:
            raise ValidationError('Failure: Phone numbers must contain 10 digits (or 11 with country code)')


class LoginForm(FlaskForm):
    username = StringField('Username', id='uname', validators=[DataRequired()])
    password = PasswordField('Password', id='pword', validators=[DataRequired()])
    two_fa = StringField('two_fa', id='2fa', validators=[validate_phone, validators.Optional()])
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', id='uname', validators=[DataRequired()])
    password = PasswordField('Password', id='pword', validators=[DataRequired()])
    two_fa = StringField('two_fa', id='2fa', validators=[validate_phone, validators.Optional()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Failure: Username is already in use')


class SubmissionForm(FlaskForm):
    inputtext = StringField('CheckText', id='inputtext', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginHistory(FlaskForm):
    userid = IntegerField('UID', id='userid', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QueryHistory(FlaskForm):
    username = StringField('Username', id='userquery', validators=[DataRequired()])
    submit = SubmitField('Submit')

