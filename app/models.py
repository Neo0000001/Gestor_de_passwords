# Importa la instancia de SQLAlchemy desde el paquete actual
from . import db


# Define el modelo 'Url', que representa una tabla de URLs
class Url(db.Model):
    # Campo 'id' como clave primaria (autoincremental)
    id = db.Column(db.Integer, primary_key=True)

    # Campo 'nombre' de la URL, debe ser único y obligatorio
    nombre = db.Column(db.String(120), unique=True, nullable=False)

    # Relación uno-a-muchos: una URL puede tener muchas entradas de contraseñas
    entradas = db.relationship("PasswordEntry", backref="url", lazy=True)


# Define el modelo 'PasswordEntry', que representa una entrada de usuario + contraseña
class PasswordEntry(db.Model):
    # Campo 'id' como clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Nombre del usuario (obligatorio)
    usuario = db.Column(db.String(120), nullable=False)

    # Contraseña cifrada (obligatoria)
    password = db.Column(db.String(256), nullable=False)  # Encriptado

    # Clave foránea que vincula la entrada con una URL específica
    url_id = db.Column(db.Integer, db.ForeignKey("url.id"), nullable=False)
