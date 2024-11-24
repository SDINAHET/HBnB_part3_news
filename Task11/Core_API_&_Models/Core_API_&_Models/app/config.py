# Configuration file for Flask environments.import os
import os

class Config:
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/development.db")


class DevelopmentConfig(Config):
    """Configuration pour le développement."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/development.db"


class TestingConfig(Config):
    """Configuration pour les tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/test.db"


class ProductionConfig(Config):
    """Configuration pour la production."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/production.db")


# Mapping des configurations
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}


# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = 'your_secret_key'
#     DEBUG = True

# class DevelopmentConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/development.db'

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/production_db'
#     DEBUG = False

# config = {
#     'default': DevelopmentConfig,
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }





# import os

# class InstanceConfig:
#     """Configuration for local development."""

#     # Secret key for Flask application
#     SECRET_KEY = os.environ.get("SECRET_KEY", "local_secret_key")

#     # Database URI for development
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         "DEV_DATABASE_URI", "sqlite:///development.db"
#     )

#     # Debug mode enabled
#     DEBUG = True

#     # Disable SQLAlchemy event tracking (improves performance)
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     # Flask-specific settings
#     WTF_CSRF_ENABLED = True
#     JSONIFY_PRETTYPRINT_REGULAR = True




# import os

# class Config:
#     """Base configuration."""
#     SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ECHO = False
#     DEBUG = False
#     TESTING = False

# class DevelopmentConfig(Config):
#     """Development configuration."""
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         'DATABASE_URL', 'sqlite:///instance/development.db'
#     )

# class TestingConfig(Config):
#     """Testing configuration."""
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         'TEST_DATABASE_URL', 'sqlite:///:memory:'
#     )
#     SQLALCHEMY_ECHO = True

# class ProductionConfig(Config):
#     """Production configuration."""
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/production.db')
#     DEBUG = False

# # Dictionary to map environment to configuration
# config_by_name = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
# }

# def get_config(env_name):
#     """Get configuration class based on environment name."""
#     return config_by_name.get(env_name, Config)





# import os

# class Config:
#     """
#     Configuration de base.
#     """
#     SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JSONIFY_PRETTYPRINT_REGULAR = True
#     CORS_HEADERS = 'Content-Type'

# class DevelopmentConfig(Config):
#     """
#     Configuration pour le développement.
#     """
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DEV_DATABASE_URI',
#         'sqlite:///development.db'
#     )

# class TestingConfig(Config):
#     """
#     Configuration pour les tests.
#     """
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'TEST_DATABASE_URI',
#         'sqlite:///test.db'
#     )
#     WTF_CSRF_ENABLED = False  # Désactiver CSRF pour faciliter les tests

# class ProductionConfig(Config):
#     """
#     Configuration pour la production.
#     """
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

# # Mapping des configurations
# config = {
#     "development": DevelopmentConfig,
#     "testing": TestingConfig,
#     "production": ProductionConfig,
#     "default": DevelopmentConfig
# }
