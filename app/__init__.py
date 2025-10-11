from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar conexión con MongoDB
    mongo.init_app(app)

    # Registrar rutas (Blueprints)
    from app.routes import main
    app.register_blueprint(main)

    print("Aplicación Flask iniciada correctamente con MongoDB")

    return app
