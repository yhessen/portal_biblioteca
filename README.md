# Portal de Biblioteca

Proyecto del parcial de TEM-742.
NEYZA ROCIO MENA HUARAYA.

Es una pagina hecha con Flask que simula el login a una biblioteca.
Tiene sesiones, cookies y plantillas con Jinja2.

## Como correrlo

1. Crear el entorno virtual:
   python -m venv venv

2. Activarlo:
   source venv/Scripts/activate

3. Instalar Flask:
   pip install flask

4. Correr la app:
   python app.py

5. Abrir en el navegador:
   http://127.0.0.1:5000/

## Usuarios para entrar

- carlos / 1111
- laura / 2222
- diego / 3333

## Que tiene cada pagina

- /          -> pagina principal
- /login     -> para iniciar sesion
- /libros    -> lista de libros
- /perfil    -> datos del usuario (hay que estar logueado)
- /logout    -> cierra sesion

## Subir a GitHub

git init
git add .
git commit -m "Proyecto inicial"
git remote add origin (link del repo)
git push -u origin main