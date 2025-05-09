# 🔐 Gestor de Contraseñas en Flask

Este proyecto es una aplicación web construida con **Flask** que permite gestionar y generar contraseñas de forma segura. Incluye funcionalidades como cifrado de contraseñas con `Fernet`, operaciones CRUD, y una interfaz simple para el usuario.

## ✨ Características

- Añadir contraseñas asociadas a URLs y usuarios.
- Cifrado seguro de contraseñas en base de datos.
- Visualización de contraseñas con opción "Mostrar/Ocultar".
- Edición y eliminación de entradas.
- Interfaz web con Flask-WTF, Jinja2 y CSS personalizado.
- Gestión de relaciones entre URLs y contraseñas (SQLAlchemy).

## 📦 Tecnologías utilizadas

- Python 3.10+
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Cryptography (Fernet)
- SQLite
- HTML + CSS + JS

## 🚀 Instalación

1. **Clona el repositorio** o descarga los archivos:

```bash
git clone https://github.com/Neo0000001/Gestor_de_passwords.git
cd gestor-passwords
```

2. **Crea un entorno virtual** y actívalo:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Genera una clave de cifrado (una sola vez):**

```bash
python generate_key.py
```

5. **Crea la base de datos:**

```bash
python crear_db.py
```

6. **Ejecuta la aplicación:**

```bash
python run.py
```

7. Abre tu navegador en: [http://localhost:5000](http://localhost:5000)

## 🧪 Funcionalidades por ruta

| Ruta                     | Funcionalidad                       |
|--------------------------|-------------------------------------|
| `/`                      | Página de inicio                    |
| `/add`                  | Añadir nueva contraseña             |
| `/passwords`             | Listar y mostrar contraseñas        |
| `/edit/<id>`             | Editar entrada                      |
| `/delete/<id>`           | Eliminar entrada                    |

## 📂 Estructura del proyecto

```
gestor_passwords/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── list.html
│   │   ├── edit.html
│   └── static/
│       ├── style.css
│       └── script.js
├── config.py
├── run.py
├── crear_db.py
├── generate_key.py
├── secret.key
├── requirements.txt
└── README.md
```

## ✅ Estado del proyecto

Proyecto en desarrollo como parte del curso de Python avanzado. Cumple con los requisitos de uso de:

- Flask y Jinja2
- SQLAlchemy con relaciones
- Formularios y validaciones
- Archivos estáticos
- Operaciones CRUD

## 🧑‍💻 Autor

Creado por Enrique Manuel Jimenez Secilla como parte del curso de Backend Python Avanzado (IBM SkillsBuild).
