# Tercera-pre-entrega-SCHAPERT

La aplicación consta de tres formularios principales:
- Creación de estudiantes
- Creación de categorías
- Creación de cursos

La idea es la siguiente:

1. Crear estudiantes
2. Crear temas (serían las categorías de los cursos)
3. Crear cursos y anotar estudiantes

Luego hay otros dos formularios que permiten:
- Obtener estudiantes según el curso
- Obtener estudiantes según su nombre o apellido

El proyecto está hecho con Django y TailwindCSS.

Instrucciones:
Ir a la carpeta del proyecto y ejecutar lo siguiente

```
virtualenv venv # o el creador de entornos virtuales que quieras
cd venv
cd scripts
activate
cd ../../
pip install django # instalamos django en el entorno virtual
cd src
python manage.py migrate
python manage.py runserver
```
