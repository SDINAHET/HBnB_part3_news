# Initialization for the app package
from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config

# Configuration globale de l'application Flask
def create_app():
    """
    Application Factory qui initialise l'app Flask avec la configuration, les routes,
    et toutes les extensions nécessaires.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Charger la configuration à partir d'une classe Config

    # Initialisation de JWT
    jwt = JWTManager(app)

    # Initialisation des blueprints de l'API
    from app.api.v1 import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
