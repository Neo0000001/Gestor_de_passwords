import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "clave-secreta-segura"  # cámbiala por algo fuerte
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "passwords.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # ← aquí desactivas CSRF temporalmente
