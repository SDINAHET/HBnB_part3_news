"""
Initialization module for the v1 API.

This module sets up the namespace and routing for the version 1 (v1) API endpoints.
"""

from flask import Blueprint
from flask_restx import Api

# Import namespaces from v1
from .routes.auth import api as auth_namespace
from .routes.users import api as users_namespace
from .routes.places import api as places_namespace
from .routes.reviews import api as reviews_namespace
from .routes.amenities import api as amenities_namespace
from .routes.protected import api as protected_namespace

# Create a Blueprint for the v1 API
v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

# Create an API instance
api = Api(
    v1_blueprint,
    title="HBnB API",
    version="1.0",
    description="API documentation for the HolbertonBnB project",
    doc="/docs"  # Swagger documentation endpoint
)

# Add namespaces to the API
api.add_namespace(auth_namespace, path='/auth')
api.add_namespace(users_namespace, path='/users')
api.add_namespace(places_namespace, path='/places')
api.add_namespace(reviews_namespace, path='/reviews')
api.add_namespace(amenities_namespace, path='/amenities')
api.add_namespace(protected_namespace, path='/protected')
