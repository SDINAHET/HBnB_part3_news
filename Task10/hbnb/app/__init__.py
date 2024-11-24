from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from config import config

# Initialisation des extensions Flask
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name='development'):
    """
    Application Factory pour configurer et initialiser l'application Flask.
    :param config_name: Nom de la configuration ('development', 'production', 'testing').
    :return: Flask app instance.
    """
    app = Flask(__name__)

    # Chargement de la configuration
    app.config.from_object(config[config_name])

    # Initialisation des extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Gestion des namespaces de l'API
    from app.api.v1.routes import api as api_v1
    api = Api(
        app,
        title="HBnB API",
        version="1.0",
        description="RESTful API for the HBnB project",
        doc="/api/v1/docs",  # Documentation Swagger
    )
    api.add_namespace(api_v1, path='/api/v1')

    return app
