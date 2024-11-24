from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

# Namespace for places
api = Namespace('places', description='Place operations')

# Define the models for Swagger documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='The title of the place'),
    'description': fields.String(required=False, description='The description of the place'),
    'price': fields.Float(required=True, description='The price per night'),
    'latitude': fields.Float(required=False, description='The latitude of the place'),
    'longitude': fields.Float(required=False, description='The longitude of the place')
})

place_update_model = api.model('PlaceUpdate', {
    'title': fields.String(description='The title of the place'),
    'description': fields.String(description='The description of the place'),
    'price': fields.Float(description='The price per night'),
    'latitude': fields.Float(description='The latitude of the place'),
    'longitude': fields.Float(description='The longitude of the place')
})

# Initialize the facade
facade = HBnBFacade()


@api.route('/')
class PlaceList(Resource):
    """Handles retrieving and creating places."""

    @api.doc('list_places')
    @jwt_required()
    def get(self):
        """
        Retrieve a list of all places.
        """
        places = facade.get_all_places()
        return [place.to_dict() for place in places], 200

    @api.doc('create_place')
    @api.expect(place_model, validate=True)
    @jwt_required()
    def post(self):
        """
        Create a new place.
        """
        current_user = get_jwt_identity()
        data = request.get_json()
        data['owner_id'] = current_user['id']  # Set the owner as the authenticated user
        new_place = facade.create_place(data)
        return new_place.to_dict(), 201


@api.route('/<string:place_id>')
class PlaceDetail(Resource):
    """Handles retrieving, updating, and deleting a specific place."""

    @api.doc('get_place')
    @jwt_required()
    def get(self, place_id):
        """
        Retrieve a specific place by ID.
        """
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'message': 'Place not found'}, 404
        return place.to_dict(), 200

    @api.doc('update_place')
    @api.expect(place_update_model, validate=True)
    @jwt_required()
    def put(self, place_id):
        """
        Update the details of a specific place.
        """
        current_user = get_jwt_identity()
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        # Ensure the authenticated user is the owner
        if place.owner_id != current_user['id']:
            return {'message': 'Unauthorized action'}, 403

        data = request.get_json()
        updated_place = facade.update_place(place_id, data)
        return updated_place.to_dict(), 200

    @api.doc('delete_place')
    @jwt_required()
    def delete(self, place_id):
        """
        Delete a specific place.
        """
        current_user = get_jwt_identity()
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        # Ensure the authenticated user is the owner
        if place.owner_id != current_user['id']:
            return {'message': 'Unauthorized action'}, 403

        facade.delete_place(place_id)
        return {'message': 'Place deleted successfully'}, 200
