from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.amenity import Amenity
from app.services.facade import HBnBFacade

# Create a namespace for amenities
api = Namespace('amenities', description='Amenity operations')

# Define the Amenity model for Swagger documentation
amenity_model = api.model('Amenity', {
    'id': fields.String(readOnly=True, description='The unique identifier of the amenity'),
    'name': fields.String(required=True, description='The name of the amenity'),
    'created_at': fields.DateTime(description='The creation date of the amenity'),
    'updated_at': fields.DateTime(description='The last update date of the amenity')
})

# Initialize the facade
facade = HBnBFacade()


@api.route('/')
class AmenityList(Resource):
    """Handles operations for all amenities."""

    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities."""
        return facade.get_all_amenities()

    @api.doc('create_amenity')
    @api.expect(amenity_model, validate=True)
    @api.marshal_with(amenity_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new amenity."""
        current_user = get_jwt_identity()
        # Ensure only admin users can create amenities
        if not facade.is_admin(current_user):
            api.abort(403, 'Admin privileges are required to perform this action.')
        data = api.payload
        return facade.create_amenity(data), 201


@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
class AmenityResource(Resource):
    """Handles operations for a single amenity."""

    @api.doc('get_amenity')
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Retrieve a specific amenity by ID."""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found.')
        return amenity

    @api.doc('update_amenity')
    @api.expect(amenity_model, validate=True)
    @api.marshal_with(amenity_model)
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity."""
        current_user = get_jwt_identity()
        # Ensure only admin users can update amenities
        if not facade.is_admin(current_user):
            api.abort(403, 'Admin privileges are required to perform this action.')
        data = api.payload
        updated_amenity = facade.update_amenity(amenity_id, data)
        if not updated_amenity:
            api.abort(404, 'Amenity not found.')
        return updated_amenity

    @api.doc('delete_amenity')
    @jwt_required()
    def delete(self, amenity_id):
        """Delete an amenity."""
        current_user = get_jwt_identity()
        # Ensure only admin users can delete amenities
        if not facade.is_admin(current_user):
            api.abort(403, 'Admin privileges are required to perform this action.')
        if not facade.delete_amenity(amenity_id):
            api.abort(404, 'Amenity not found.')
        return {'message': 'Amenity deleted successfully'}, 200
