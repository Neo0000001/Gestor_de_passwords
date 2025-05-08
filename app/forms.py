from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class PasswordForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired(), Length(min=3, max=120)])
    usuario = StringField(
        "Usuario", validators=[DataRequired(), Length(min=3, max=120)]
    )
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8, max=128)]
    )
    submit = SubmitField("Guardar")
