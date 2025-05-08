from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import PasswordForm
from .models import db, Url, PasswordEntry
from cryptography.fernet import Fernet

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/add", methods=["GET", "POST"])
def add_password():
    form = PasswordForm()
    if form.validate_on_submit():
        # Buscar o crear la URL
        url_obj = Url.query.filter_by(nombre=form.url.data).first()
        if not url_obj:
            url_obj = Url(nombre=form.url.data)
            db.session.add(url_obj)
            db.session.commit()

        # Cifrar la contraseña antes de guardarla
        encrypted_password = fernet.encrypt(form.password.data.encode()).decode()

        entry = PasswordEntry(
            usuario=form.usuario.data,
            password=encrypted_password,
            url_id=url_obj.id,
        )

        db.session.add(entry)
        db.session.commit()

        flash("Contraseña guardada con éxito.", "success")
        return redirect(url_for("main.index"))

    return render_template("add.html", form=form)


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


fernet = Fernet(load_key())


@main.route("/passwords")
def list_passwords():
    from .models import PasswordEntry

    entries = PasswordEntry.query.all()

    # Descifrar las contraseñas antes de pasarlas a la plantilla
    decrypted_entries = []
    for entry in entries:
        decrypted_password = fernet.decrypt(entry.password.encode()).decode()
        decrypted_entries.append(
            {
                "id": entry.id,
                "usuario": entry.usuario,
                "password": decrypted_password,
                "url": entry.url.nombre,  # usando la relación
            }
        )

    return render_template("list.html", entries=decrypted_entries)


@main.route("/delete/<int:entry_id>", methods=["POST"])
def delete_password(entry_id):
    entry = PasswordEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entrada eliminada correctamente.", "success")
    return redirect(url_for("main.list_passwords"))


@main.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit_password(entry_id):
    entry = PasswordEntry.query.get_or_404(entry_id)
    form = PasswordForm()

    if form.validate_on_submit():
        entry.usuario = form.usuario.data
        entry.password = fernet.encrypt(form.password.data.encode()).decode()
        db.session.commit()
        flash("Entrada actualizada correctamente.", "success")
        return redirect(url_for("main.list_passwords"))

    # Rellenar el formulario con los datos actuales
    form.url.data = entry.url.nombre  # solo visual, no editable aquí
    form.usuario.data = entry.usuario
    form.password.data = fernet.decrypt(entry.password.encode()).decode()

    return render_template("edit.html", form=form, entry=entry)
