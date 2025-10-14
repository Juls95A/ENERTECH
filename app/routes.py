
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


# Ruta para Login
@main.route('/login')
def login():
    return render_template('Login.html')

# Ruta para Registro
@main.route('/registrarse')
def registrarse():
    return render_template('Registrarse.html')
