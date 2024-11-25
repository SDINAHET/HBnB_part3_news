# Initialize sub-routes.
from app.api.v1.routes import users, places, reviews, amenities, auth

v1_bp.register_blueprint(users.bp, url_prefix='/users')
v1_bp.register_blueprint(places.bp, url_prefix='/places')
v1_bp.register_blueprint(reviews.bp, url_prefix='/reviews')
v1_bp.register_blueprint(amenities.bp, url_prefix='/amenities')
v1_bp.register_blueprint(auth.bp, url_prefix='/auth')
