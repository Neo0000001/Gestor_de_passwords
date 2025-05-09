# Importa herramientas de Flask
from flask import Blueprint, render_template, redirect, url_for, flash

# Importa el formulario para añadir/editar contraseñas
from .forms import PasswordForm

# Importa los modelos y la base de datos
from .models import db, Url, PasswordEntry

# Importa Fernet para cifrado simétrico de contraseñas
from cryptography.fernet import Fernet

# Crea un Blueprint llamado 'main' para organizar las rutas
main = Blueprint("main", __name__)


# Ruta principal que muestra la página de inicio
@main.route("/")
def index():
    return render_template("index.html")


# Ruta para añadir una nueva contraseña
@main.route("/add", methods=["GET", "POST"])
def add_password():
    form = PasswordForm()

    # Verifica si el formulario ha sido enviado correctamente
    if form.validate_on_submit():
        # Busca si la URL ya existe en la base de datos
        url_obj = Url.query.filter_by(nombre=form.url.data).first()
        # Si no existe, la crea y la guarda
        if not url_obj:
            url_obj = Url(nombre=form.url.data)
            db.session.add(url_obj)
            db.session.commit()

        # Cifra la contraseña usando Fernet
        encrypted_password = fernet.encrypt(form.password.data.encode()).decode()

        # Crea una nueva entrada de contraseña
        entry = PasswordEntry(
            usuario=form.usuario.data,
            password=encrypted_password,
            url_id=url_obj.id,
        )

        # Guarda la entrada en la base de datos
        db.session.add(entry)
        db.session.commit()

        # Muestra un mensaje de éxito y redirige al inicio
        flash("Contraseña guardada con éxito.", "success")
        return redirect(url_for("main.index"))

    # Si la petición es GET o el formulario no es válido, muestra el formulario
    return render_template("add.html", form=form)


# Función para cargar la clave de cifrado desde el archivo 'secret.key'
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


# Instancia de Fernet creada con la clave cargada
fernet = Fernet(load_key())


# Ruta para listar todas las contraseñas guardadas
@main.route("/passwords")
def list_passwords():
    from .models import PasswordEntry

    # Obtiene todas las entradas
    entries = PasswordEntry.query.all()

    # Descifra cada contraseña antes de enviarla a la plantilla
    decrypted_entries = []
    for entry in entries:
        decrypted_password = fernet.decrypt(entry.password.encode()).decode()
        decrypted_entries.append(
            {
                "id": entry.id,
                "usuario": entry.usuario,
                "password": decrypted_password,
                "url": entry.url.nombre,  # Accede al nombre mediante la relación con URL
            }
        )

    return render_template("list.html", entries=decrypted_entries)


# Ruta para eliminar una entrada específica por su ID
@main.route("/delete/<int:entry_id>", methods=["POST"])
def delete_password(entry_id):
    entry = PasswordEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entrada eliminada correctamente.", "success")
    return redirect(url_for("main.list_passwords"))


# Ruta para editar una entrada existente
@main.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit_password(entry_id):
    entry = PasswordEntry.query.get_or_404(entry_id)
    form = PasswordForm()

    # Si el formulario es válido, actualiza los datos
    if form.validate_on_submit():
        entry.usuario = form.usuario.data
        entry.password = fernet.encrypt(form.password.data.encode()).decode()
        db.session.commit()
        flash("Entrada actualizada correctamente.", "success")
        return redirect(url_for("main.list_passwords"))

    # Prellenar el formulario con los datos actuales (solo para mostrar)
    form.url.data = entry.url.nombre  # solo visual, no editable aquí
    form.usuario.data = entry.usuario
    form.password.data = fernet.decrypt(entry.password.encode()).decode()

    return render_template("edit.html", form=form, entry=entry)
