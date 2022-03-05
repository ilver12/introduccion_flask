from distutils.log import debug
from pydoc import render_doc
from sqlite3 import Cursor
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ilver',
    port=3306,
    database='productos'
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def inicio():
    cursor = db.cursor(dictionary = True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall() #obtener todo
    #producto = cursor.fetchone()
    print(productos)

    cursor.close()

    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    #recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')

    #insertar los datos en la base de datos
    cursor = db.cursor()
    cursor.execute("insert into productos(nombre,price) values(%s,%s)",(
        nombre,
        price,
    ))
    cursor.close()
    #volver al listado
    return redirect(url_for('inicio'))

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id=contactoId)

#edad/20

@app.get("/edad/<int:edadId>")
def edad(edadId):
    return render_template("edad.html", id=edadId)

app.run(debug=True)