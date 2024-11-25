# Local configuration.
import os

# Configuration spécifique à l'environnement local
class InstanceConfig:
    # Clé secrète pour l'application Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "local_secret_key")

    # Base de données pour l'environnement de développement
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URI", "sqlite:///development.db"
    )

    # Activation du mode débogage
    DEBUG = True

    # Désactivation du suivi des modifications SQLAlchemy (recommandé pour de meilleures performances)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Autres configurations spécifiques
    WTF_CSRF_ENABLED = True
    JSONIFY_PRETTYPRINT_REGULAR = True
