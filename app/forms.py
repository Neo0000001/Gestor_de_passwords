# Importa la clase base FlaskForm para crear formularios con Flask-WTF
from flask_wtf import FlaskForm

# Importa tipos de campos que se usarán en el formulario
from wtforms import StringField, PasswordField, SubmitField

# Importa validadores para asegurar que los datos sean correctos
from wtforms.validators import DataRequired, Length


# Define una clase de formulario llamada PasswordForm, que hereda de FlaskForm
class PasswordForm(FlaskForm):
    # Campo para la URL, obligatorio y con longitud entre 3 y 120 caracteres
    url = StringField("URL", validators=[DataRequired(), Length(min=3, max=120)])

    # Campo para el nombre de usuario, obligatorio y con longitud entre 3 y 120
    usuario = StringField(
        "Usuario", validators=[DataRequired(), Length(min=3, max=120)]
    )

    # Campo para la contraseña, obligatorio y con longitud mínima de 8 caracteres
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8, max=128)]
    )

    # Botón de envío del formulario
    submit = SubmitField("Guardar")
