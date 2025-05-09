# Importa la función create_app y el objeto db desde el módulo app
from app import create_app, db

# Crea una instancia de la aplicación Flask usando la función factory create_app
app = create_app()

# Activa el contexto de la aplicación para que operaciones como acceso a la base de datos funcionen correctamente
with app.app_context():
    # Crea todas las tablas definidas en los modelos (si no existen) en la base de datos
    db.create_all()

    # Imprime un mensaje indicando que la base de datos se ha creado correctamente
    print("Base de datos creada con éxito.")
