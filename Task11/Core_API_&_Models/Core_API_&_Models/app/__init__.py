# Entry point for running the Flask application.from flask import Flask
# from flask import Flask
# from app.config import config

# def create_app(config_name="default"):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(config[config_name])

#     # Import et enregistrement des blueprints
#     from app.api.v1.routes import api_v1
#     app.register_blueprint(api_v1, url_prefix='/api/v1')

#     return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from flasgger import Swagger
# from config import InstanceConfig

# # Initialize extensions
# db = SQLAlchemy()
# ma = Marshmallow()

# def create_app(config_name="config.InstanceConfig"):
#     app = Flask(__name__, instance_relative_config=True)

#     # Load configuration
#     app.config.from_object(config_name)
#     app.config.from_pyfile('config.py', silent=True)

#     # Initialize extensions
#     db.init_app(app)
#     ma.init_app(app)
#     CORS(app)

#     # Initialize Swagger
#     swagger = Swagger(app)

#     # Register blueprints
#     from app.api.vi.routes import users, places, reviews, amenities, auth

#     app.register_blueprint(users.bp, url_prefix='/api/vi/users')
#     app.register_blueprint(places.bp, url_prefix='/api/vi/places')
#     app.register_blueprint(reviews.bp, url_prefix='/api/vi/reviews')
#     app.register_blueprint(amenities.bp, url_prefix='/api/vi/amenities')
#     app.register_blueprint(auth.bp, url_prefix='/api/vi/auth')

#     # Root route
#     @app.route('/')
#     def index():
#         return {"message": "Welcome to the API. Refer to /apidocs for API documentation."}, 200

#     # Error handlers
#     @app.errorhandler(404)
#     def not_found_error(error):
#         return {"error": "Not found"}, 404

#     @app.errorhandler(500)
#     def internal_error(error):
#         return {"error": "Internal server error"}, 500

#     return app


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flasgger import Swagger
# from app.api.v1.routes import users, amenities, places, reviews, auth

from flask import Flask
from app.config import config
# from app.api.v1 import v1_bp  # Import du Blueprint principal pour l'API v1

# Extensions
# db = SQLAlchemy()
# ma = Marshmallow()

def create_app(config_name="default"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    app.config['JWT_SECRET_KEY'] = 'default_secret_key' #add SD
    # Enregistrer le Blueprint principal pour l'API v1
    # app.register_blueprint(v1_bp, url_prefix="/api/v1")


    # Route de test


    # Initialiser les extensions
    # db.init_app(app)
    # ma.init_app(app)
    # CORS(app)
    # bcrypt.init_app(app)
    # jwt.init_app(app)

    # Swagger configuration
    # swagger()

    # bp = Api(app, version='1.0',
    #         title='HBnB API',
    #         description='HBnB Application API',
    #         security='Bearer Auth', # Add SD
    #         authorizations={ # Add SD
    #           'Bearer Auth': {
    #               'type': 'apiKey',
    #               'in': 'header',
    #               'name': 'Authorization',
    #               'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
    #             }
    #       })
    # Enregistrer les Blueprints
    # from app.api.v1.routes import users, amenities, places, reviews, auth

    # app.register_blueprint(users.bp, url_prefix="/api/v1/users")
    # app.register_blueprint(amenities.bp, url_prefix="/api/v1/amenities")
    # app.register_blueprint(places.bp, url_prefix="/api/v1/places")
    # app.register_blueprint(reviews.bp, url_prefix="/api/v1/reviews")
    # app.register_blueprint(auth.bp, url_prefix="/api/v1/auth")

    @app.route('/test', methods=['GET'])
    def test():
        return {"message": "Test route works!"}, 200

    # Afficher toutes les routes enregistrées pour déboguer
    for rule in app.url_map.iter_rules():
        print(f"Route: {rule.endpoint} -> {rule}")

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


# from flask import Flask
# from flask_restx import Api
# from app.extension import bcrypt, jwt, db
# from config import config
# from app.api.v1 import create_api_v1

# def create_app(config_name="default"):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#     app.config['JWT_SECRET_KEY'] = 'default_secret_key'  # Clé JWT par défaut

#     # Initialiser les extensions
#     bcrypt.init_app(app)
#     jwt.init_app(app)
#     db.init_app(app)

#     # Créer et enregistrer l'API v1
#     api_v1 = create_api_v1()
#     app.register_blueprint(api_v1, url_prefix='/api/v1')

#     return app



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from flasgger import Swagger
# from app.config import config

# # Initialisation des extensions
# db = SQLAlchemy()
# ma = Marshmallow()

# def create_app(config_name="default"):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(config[config_name])

#     # Initialiser les extensions
#     db.init_app(app)
#     ma.init_app(app)
#     CORS(app)

#     # Configuration de Swagger
#     swagger_config = {
#         "headers": [],
#         "specs": [
#             {
#                 "endpoint": "apispec",
#                 "route": "/apispec.json",
#                 "rule_filter": lambda rule: True,  # Inclut toutes les routes
#                 "model_filter": lambda tag: True,  # Inclut tous les modèles
#             }
#         ],
#         "static_url_path": "/flasgger_static",
#         "swagger_ui": True,
#         "specs_route": "/apidocs/",
#     }
#     Swagger(app, config=swagger_config)

#     # Enregistrer les Blueprints
#     from app.api.v1.routes import users, amenities, places, reviews, auth
#     app.register_blueprint(users.bp, url_prefix="/api/v1/users")
#     app.register_blueprint(amenities.bp, url_prefix="/api/v1/amenities")
#     app.register_blueprint(places.bp, url_prefix="/api/v1/places")
#     app.register_blueprint(reviews.bp, url_prefix="/api/v1/reviews")
#     app.register_blueprint(auth.bp, url_prefix="/api/v1/auth")

#     return app


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from flasgger import Swagger

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

#     # Configuration Swagger
#     Swagger(app)

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

