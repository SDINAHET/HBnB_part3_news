# Initialize the API package.
from flask import Blueprint

# Crée le blueprint principal pour l'API
api_bp = Blueprint('api', __name__)

# Importe les blueprints des différentes versions de l'API
from app.api.v1 import v1_bp

# Enregistre les blueprints des versions
api_bp.register_blueprint(v1_bp, url_prefix='/v1')
