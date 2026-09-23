from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = "biblioteca123" 

usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}

libros = [
    {"titulo": "Python desde cero", "autor": "Juan Perez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "Maria Lopez", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro Garcia", "disponibles": 0}
]


# Pagina principal: lee la cookie ultimo_usuario y el mensaje de logout
@app.route("/")
def index():
    ultimo_usuario = request.cookies.get("ultimo_usuario")
    cerro_sesion = request.args.get("mensaje") 
    return render_template("index.html", ultimo_usuario=ultimo_usuario, cerro_sesion=cerro_sesion)


# Ruta de login: valida usuario y contraseña contra el diccionario "usuarios"
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        if usuario in usuarios and usuarios[usuario] == password:
            session["usuario"] = usuario

            resp = make_response(redirect(url_for("libros_view")))
            resp.set_cookie("ultimo_usuario", usuario, max_age=604800)  
            return resp

        error = "Usuario o contraseña incorrectos."

    return render_template("login.html", error=error)


@app.route("/libros")
def libros_view():
    usuario = session.get("usuario")
    return render_template("libros.html", libros=libros, usuario=usuario)


# Ruta protegida: si no hay sesion activa, redirige al login
@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("perfil.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index", mensaje="ok"))


@app.route("/borrar-cookie")
def borrar_cookie():
    resp = make_response(redirect(url_for("index")))
    resp.delete_cookie("ultimo_usuario")
    return resp


if __name__ == "__main__":
    app.run(debug=True)