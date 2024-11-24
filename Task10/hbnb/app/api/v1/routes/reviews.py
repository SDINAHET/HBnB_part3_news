from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

# Namespace pour les reviews
api = Namespace('reviews', description='Routes for managing reviews')

# Modèles pour la documentation Swagger/Restx
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Review text'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place being reviewed')
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(required=False, description='Updated review text'),
    'rating': fields.Integer(required=False, description='Updated rating (1-5)')
})

facade = HBnBFacade()

@api.route('/')
class ReviewList(Resource):
    """Gestion des reviews (création et récupération)"""

    @jwt_required()
    @api.expect(review_model)
    def post(self):
        """Créer une nouvelle review"""
        current_user = get_jwt_identity()
        data = api.payload

        # Validation des données
        if not (1 <= data['rating'] <= 5):
            return {'message': 'Rating must be between 1 and 5'}, 400

        try:
            review = facade.create_review(
                user_id=current_user['id'],
                place_id=data['place_id'],
                text=data['text'],
                rating=data['rating']
            )
            return {'message': 'Review created successfully', 'review': review.to_dict()}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.doc('get_reviews')
    def get(self):
        """Récupérer toutes les reviews"""
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200


@api.route('/<string:review_id>')
class ReviewResource(Resource):
    """Gestion d'une review spécifique"""

    @jwt_required()
    def get(self, review_id):
        """Récupérer une review par ID"""
        review = facade.get_review_by_id(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        return review.to_dict(), 200

    @jwt_required()
    @api.expect(review_update_model)
    def put(self, review_id):
        """Mettre à jour une review"""
        current_user = get_jwt_identity()
        data = api.payload

        try:
            updated_review = facade.update_review(
                review_id=review_id,
                user_id=current_user['id'],
                data=data
            )
            if updated_review is None:
                return {'message': 'Unauthorized or review not found'}, 403
            return {'message': 'Review updated successfully', 'review': updated_review.to_dict()}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    @jwt_required()
    def delete(self, review_id):
        """Supprimer une review"""
        current_user = get_jwt_identity()
        success = facade.delete_review(review_id, user_id=current_user['id'])
        if not success:
            return {'message': 'Unauthorized or review not found'}, 403
        return {'message': 'Review deleted successfully'}, 200
