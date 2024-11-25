# Initialize API v1 routes.
from flask import Blueprint

# Crée le blueprint pour l'API v1
v1_bp = Blueprint('v1', __name__)

# Importe les routes spécifiques
from app.api.v1.routes import users, places, reviews, amenities, auth

# Enregistre les blueprints ou routes individuelles si nécessaire
v1_bp.register_blueprint(users.bp, url_prefix='/users')
v1_bp.register_blueprint(places.bp, url_prefix='/places')
v1_bp.register_blueprint(reviews.bp, url_prefix='/reviews')
v1_bp.register_blueprint(amenities.bp, url_prefix='/amenities')
v1_bp.register_blueprint(auth.bp, url_prefix='/auth')
