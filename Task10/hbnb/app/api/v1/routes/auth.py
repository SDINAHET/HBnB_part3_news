from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import create_access_token
from app.services.facade import HBnBFacade
from werkzeug.security import check_password_hash
import datetime

# Namespace for authentication
api = Namespace('auth', description='Authentication operations')

# Define models for Swagger documentation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})

# Initialize the facade
facade = HBnBFacade()


@api.route('/login')
class Login(Resource):
    """Handles user login to retrieve JWT tokens."""

    @api.doc('login_user')
    @api.expect(login_model, validate=True)
    def post(self):
        """
        Authenticate user and return a JWT token.
        """
        # Get the credentials from the request
        credentials = request.get_json()
        email = credentials.get('email')
        password = credentials.get('password')

        # Fetch the user by email
        user = facade.get_user_by_email(email)
        if not user:
            return {'message': 'Invalid email or password'}, 401

        # Verify the password
        if not check_password_hash(user.password, password):
            return {'message': 'Invalid email or password'}, 401

        # Create the JWT token
        token = create_access_token(
            identity={'id': user.id, 'is_admin': user.is_admin},
            expires_delta=datetime.timedelta(hours=24)
        )

        return {'token': token, 'user': user.to_dict()}, 200
