from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# Namespace pour les routes protégées
api = Namespace('protected', description='Protected routes requiring authentication')

@api.route('/user-profile')
class UserProfile(Resource):
    """Endpoint pour récupérer les informations du profil utilisateur connecté."""

    @jwt_required()
    def get(self):
        """
        Retourne le profil de l'utilisateur authentifié.
        """
        # Récupère l'identité utilisateur depuis le token JWT
        current_user = get_jwt_identity()

        # Renvoie l'identité (ID utilisateur et rôle is_admin)
        return {
            'message': 'User profile retrieved successfully',
            'user': current_user
        }, 200


@api.route('/admin-only')
class AdminOnly(Resource):
    """Endpoint accessible uniquement aux administrateurs."""

    @jwt_required()
    def get(self):
        """
        Vérifie si l'utilisateur est admin et renvoie une réponse.
        """
        # Récupère l'identité utilisateur depuis le token JWT
        current_user = get_jwt_identity()

        if not current_user.get('is_admin'):
            return {'message': 'Access denied: Admins only'}, 403

        return {
            'message': 'Welcome, admin!',
            'user': current_user
        }, 200
