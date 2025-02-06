from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config["MYSQL_HOST"] = config.Config.MYSQL_HOST
app.config["MYSQL_USER"] = config.Config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = config.Config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = config.Config.MYSQL_DB
app.config["MYSQL_PORT"] = config.Config.MYSQL_PORT

# Inicializar la base de datos
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/spa")
def spa():
    return render_template("spa.html")


@app.route("/form", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        # Obtener datos del formulario
        nombre = request.form.get("nombre").strip()
        apellido = request.form.get("apellido").strip()
        telefono = request.form.get("telefono").strip()
        email = request.form.get("email").strip()

        # Guardar los datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Users (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s)",
            (nombre, apellido, telefono, email),
        )
        mysql.connection.commit()
        cur.close()

        # Redirigir al formulario
        return redirect(url_for("formulario"))

    return render_template("form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
