from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Ruta para mostrar el formulario principal en el navegador
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta para recibir los datos del formulario por POST y guardarlos en MySQL
@app.route("/incidencias", methods=["POST"])
def crear_incidencia():
    # Recogemos los datos exactamente como se llaman en el formulario HTML
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    puesto = request.form["puesto"]

    # Conexión directa a la base de datos 'Concello'
    connexion = mysql.connector.connect(
        host="localhost",
        user="concello",
        password="concello",
        database="Concello"
    )
    cursor = connexion.cursor()

    
    sql = "INSERT INTO registro (dni, nombre, direccion, puesto) VALUES (%s, %s, %s, %s)"
    valores = (dni, nombre, direccion, puesto)
    
    cursor.execute(sql, valores)
    connexion.commit()
    
    cursor.close()
    connexion.close()

   
    return f"<h1>Incidencia guardada correctamente para: {nombre}</h1><a href='/'>Volver al inicio</a>"

if __name__ == "__main__":
    app.run(debug=True)