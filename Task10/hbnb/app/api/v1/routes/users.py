from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

# Namespace pour les utilisateurs
api = Namespace('users', description='Routes for managing users')

# Modèles pour la documentation Swagger/Restx
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email address of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(required=False, description='Updated first name'),
    'last_name': fields.String(required=False, description='Updated last name'),
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    """Gestion des utilisateurs : création et récupération"""

    @jwt_required()
    def get(self):
        """Récupérer tous les utilisateurs (admin uniquement)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'message': 'Admin privileges required'}, 403

        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200

    @api.expect(user_model)
    def post(self):
        """Créer un nouvel utilisateur"""
        data = api.payload

        try:
            user = facade.create_user(data)
            return {'message': 'User created successfully', 'user': user.to_dict()}, 201
        except ValueError as e:
            return {'message': str(e)}, 400


@api.route('/<string:user_id>')
class UserResource(Resource):
    """Gestion d'un utilisateur spécifique"""

    @jwt_required()
    def get(self, user_id):
        """Récupérer un utilisateur par ID (admin ou utilisateur connecté)"""
        current_user = get_jwt_identity()
        if not (current_user.get('is_admin') or current_user['id'] == user_id):
            return {'message': 'Unauthorized access'}, 403

        user = facade.get_user_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.to_dict(), 200

    @jwt_required()
    @api.expect(user_update_model)
    def put(self, user_id):
        """Mettre à jour un utilisateur"""
        current_user = get_jwt_identity()
        if not (current_user.get('is_admin') or current_user['id'] == user_id):
            return {'message': 'Unauthorized action'}, 403

        data = api.payload

        try:
            updated_user = facade.update_user(user_id=user_id, data=data)
            if not updated_user:
                return {'message': 'User not found'}, 404
            return {'message': 'User updated successfully', 'user': updated_user.to_dict()}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    @jwt_required()
    def delete(self, user_id):
        """Supprimer un utilisateur (admin uniquement)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'message': 'Admin privileges required'}, 403

        success = facade.delete_user(user_id)
        if not success:
            return {'message': 'User not found'}, 404
        return {'message': 'User deleted successfully'}, 200
