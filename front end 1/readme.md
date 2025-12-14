# Servicopiapo Propiedades

Sistema web para la gestión y publicación de propiedades inmobiliarias. Permite a los administradores agregar, actualizar y eliminar propiedades, y a los clientes explorar las propiedades disponibles.

---

## Tecnologías
- Python 3.x
- Django 4.x
- Bootstrap 5
- HTML / CSS / JavaScript
- mySQL

---
## Instrucciones

####  Clonar el repositorio
#### Crear y activar un entorno virtual
**Windows**
python -m venv env
env\Scripts\activate

**macOS / Linux**
python3 -m venv env
source env/bin/activate

#### Instalar dependencias
pip install -r requirements.txt

#### Ejecutar las migraciones
python manage.py makemigrations
python manage.py migrate

#### Iniciar el servidor de desarrollo
python manage.py runserver

#### Notas
- Requiere un **usuario staff o superusuario** para acceder al panel de gestión.
