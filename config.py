# Importa el módulo os para trabajar con rutas y archivos del sistema
import os

# Obtiene la ruta absoluta del directorio donde se encuentra este archivo
basedir = os.path.abspath(os.path.dirname(__file__))


# Define una clase de configuración que se usará en la app Flask
class Config:
    # Clave secreta para la aplicación (usada en sesiones, formularios, etc.)
    # Es recomendable cambiarla por una clave fuerte y segura en producción
    SECRET_KEY = "clave-secreta-segura"  # cámbiala por algo fuerte

    # URI de conexión a la base de datos SQLite, en este caso un archivo llamado passwords.db
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "passwords.db")

    # Desactiva el sistema de seguimiento de modificaciones de objetos en SQLAlchemy (mejora el rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Desactiva temporalmente la protección CSRF en formularios (solo recomendable en desarrollo)
    WTF_CSRF_ENABLED = False  # ← aquí desactivas CSRF temporalmente
