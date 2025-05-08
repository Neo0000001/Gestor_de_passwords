from . import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    entradas = db.relationship("PasswordEntry", backref="url", lazy=True)


class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False)  # Encriptado
    url_id = db.Column(db.Integer, db.ForeignKey("url.id"), nullable=False)
