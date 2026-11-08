from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# crear base de datos sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.string(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f'<Producto {self.nombre}>'
    
    
# ruta al index y lectura de productos
@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos = productos)

@app.route('/crear', methods=['POST'])
def crear():
    nombre_input = request.form['nombre']
    precio_input = request.form['precio']
    
    nuevo_producto = Producto(nombre=nombre_input, precio=float(precio_input))
    
    db.session.add(nuevo_producto)
    db.session.commit()
    
    return redirect(url_for('index'))