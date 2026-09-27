# Manual de intalacion de la aplicacion web 

## Crear respositorio git

Tienes que estar dentro de /var

1. Crear git

`git init`

2. Crear

`git add .`

3. Añadir un comentario
`git commit -m "Commit inicial con readme y página principal con formulario web"`


## Proceso de instalacion / puesta en marcha

1. Actualicacion sistema
`sudo apt update`
`sudo apt upgrade`
2. Instalar git
`sudo apt install git`
3. Instalar VSCODE + plugins:

    - Markdown all in one

4. Instalar apache2

`sudo apt install apache2`

5. Cambiar permisos carpeta /var/www/html

``` bash 
sudo chown -R $USER:$USER /var/www/html

sudo chmod -R u=rwx,go=rx /var/www/html
```

1. Instalar mysql server
   
```bash

sudo apt install mysql-servers

```

# Creacion de la base de datos

# Entrar en SQL

```bash

1. sudo mysql

2. mysql> create database Concello;

3. mysql> create user 'Concello'@'localhost' identified by 'Concello';

4. mysql> grant all privileges on Concello.* to  'Concello'@'localhost';

5. mysql> flush privileges;



```

1. usar tabla mysql> use incidencias;

2. cree tabala mysql> create table registro( -> id varchar auto_increment primary key, -> aula varchar(30), -> descripcion text, -> usuario varchar(20), -> estado verchar(30) -> );


3. mysql> INSERT INTO registro (dni, nombre, direccion, puesto) 
VALUES ('12345678A', 'Juan Pérez', 'Calle Falsa 123', 'Desarrollador');

## Configuracion de git/github

```bash

git status-> para ver el estado 

git add . -->para añadir lo nuevo git 

commit -m "comentarios" ---> añade comentarios 

git push --> subir al githab

```

## Instalar python

Esto lo haces dentro de /var/www/la carpeta de tu proyecto

```bash
sudo apt install python3 python3-pip python3-venv -y

```

1. Crear el entorno virtual y activarlo

```bash

python3 -m venv venv
```

```bash

source venv/bin/activate

alumno@pc-xx:/var/www/municipio$  source /var/www/municipio/venv/bin/activate

```

2. Instalar flack, conector de bases de datos , comprobar y guardar las dependencias

```bash
pip install flask
pip install mysql-connector-python
pip list
pip freeze >requirements.txt

```

Salirse del entorno virtual

```bash

deactivate

```

3. Hacer el gitingnore

Poner dentro del archivo .gitignore

```bash

venv/
_pycache__\
*.pyc
.env


```

# Rutina de trabajo con flask (venv)

Para comenzar la aplicacion:

```bash


source venv/bin/activate
python app.by 'iniciar aplicacion'

control c para terminar

```

# Hacer aplicacion de python 

```bash

from flask import Flask

app = Flask(_name_)

@app.route("/")
def inicio():
    return "<h1>Incidencias IES Teis</h1>"

if _name_=="_main_":
    app.run(debug=True)

```

Ejecutamos

```bash
cd /var/www/municipio
source venv/bin/activate

python3 app.py


```

Comprobamos en http://municipio:5000

# Migracion del formulario a python/falsk

1.Creamos una carpeta templates y movemos ahi nuestro index.html

2. modificamos app.py;

```bash
from flask import Flask, render_template, request

app = Flask(__name__)

@app.router("/")
def inicio():
     return render_template("index.html")

 if _name_=="_name_":
     app.run(debug=True)


```


## Recibir los datos del formulario

3. Añadimos una ruta en app.py para recibir los datos del formulario:

```bash
@app.route("/incidencias", methods=["POST"])
def crear_incidencia():
    # Recogemos los datos exactamente como se llaman en el formulario HTML
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    puesto = request.form["puesto"]


```

# Documunto app.py con:

1. Recibir datos del formulario

2. Visualizacion en pantalla

3. Añadir datos a la BD



```bash

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


```


Comandos de la base de datos:


Ver usuarios

```bash
select user,host from mysql.user;


```

Para ver datos de una tabla:

```bash


select * from registro;
```