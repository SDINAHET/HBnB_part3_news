# Initialize API v1 routes.
from flask import Blueprint
from app.api.v1.routes import users, places, reviews, amenities, auth
# Crée le blueprint pour l'API v1
# v1_bp = Blueprint('v1', __name__)
v1_bp = Blueprint("v1", __name__, url_prefix="/api/v1")

# Importe les routes spécifiques
# from app.api.v1.routes import users, places, reviews, amenities, auth
# Importer les routes
# from .routes import users, amenities, places, reviews, auth

# Enregistre les blueprints ou routes individuelles si nécessaire
v1_bp.register_blueprint(users.bp, url_prefix='/users')
v1_bp.register_blueprint(places.bp, url_prefix='/places')
v1_bp.register_blueprint(reviews.bp, url_prefix='/reviews')
v1_bp.register_blueprint(amenities.bp, url_prefix='/amenities')
v1_bp.register_blueprint(auth.bp, url_prefix='/auth')
