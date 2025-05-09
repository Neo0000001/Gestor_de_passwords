# Importa la clase Flask para crear la aplicación web
from flask import Flask

# Importa la clase SQLAlchemy para gestionar la base de datos
from flask_sqlalchemy import SQLAlchemy

# Importa la clase de configuración desde un archivo externo llamado config.py
from config import Config

# Crea una instancia de SQLAlchemy (sin enlazar aún a ninguna app)
db = SQLAlchemy()


# Define una función factory que crea y configura la app de Flask
def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Carga la configuración desde el objeto Config (por ejemplo, la URI de la base de datos)
    app.config.from_object(Config)

    # Inicializa la extensión SQLAlchemy con la aplicación Flask
    db.init_app(app)

    # Importa las rutas (blueprint principal) desde el paquete actual
    from .routes import main

    # Registra el blueprint 'main' en la app
    app.register_blueprint(main)

    # Devuelve la aplicación ya configurada
    return app
