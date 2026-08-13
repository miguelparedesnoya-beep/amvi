# AMVI — Plataforma Web

Proyecto Django para la Asociación de Productores Multiactivos de Villa Isabel.

## Instalación en Windows

```powershell
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## MySQL

Crear la base de datos:

```sql
CREATE DATABASE amvi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Por defecto Django usa:
- Base: amvi_db
- Usuario: root
- Contraseña: vacía
- Host: 127.0.0.1
- Puerto: 3306

Si necesitas otros datos, define las variables DB_NAME, DB_USER, DB_PASSWORD, DB_HOST y DB_PORT.

## Migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir:
- Web: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Las imágenes subidas por el administrador se guardan en `media/`.
