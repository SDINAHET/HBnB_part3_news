# Entry point for running the Flask application.from flask import Flask
from flask import Flask
from app.config import config

def create_app(config_name="default"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    return app





# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from flask import Flask
# # from config import InstanceConfig
# from config import Config
# # from app.config import config

# # Initialisation des extensions
# db = SQLAlchemy()
# ma = Marshmallow()

# def create_app(config_name="config.Config"):
#     """
#     Crée et configure l'application Flask.

#     Args:
#         config_name (str): Chemin vers la configuration de l'application.
#                            Par défaut : 'config.Config'.

#     Returns:
#         Flask: Instance de l'application Flask.
#     """
#     app = Flask(__name__, instance_relative_config=True)

#     # Chargement de la configuration
#     app.config.from_object(config_name)
#     app.config.from_pyfile('config.py', silent=True)

#     # Initialisation des extensions
#     db.init_app(app)
#     ma.init_app(app)
#     CORS(app)

#     # Enregistrement des blueprints
#     from app.api.v1.routes import users, places, reviews, amenities, auth

#     app.register_blueprint(users.bp, url_prefix='/api/v1/users')
#     app.register_blueprint(places.bp, url_prefix='/api/v1/places')
#     app.register_blueprint(reviews.bp, url_prefix='/api/v1/reviews')
#     app.register_blueprint(amenities.bp, url_prefix='/api/v1/amenities')
#     app.register_blueprint(auth.bp, url_prefix='/api/v1/auth')

#     # Gestion des erreurs personnalisées
#     @app.errorhandler(404)
#     def not_found_error(error):
#         return {"error": "Not found"}, 404

#     @app.errorhandler(500)
#     def internal_error(error):
#         return {"error": "Internal server error"}, 500

#     return app
