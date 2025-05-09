# Importa la función create_app desde el módulo app
from app import create_app

# Crea una instancia de la aplicación Flask usando la función create_app
app = create_app()

# Si este archivo se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Inicia el servidor de desarrollo de Flask con modo debug activado
    app.run(debug=True)
