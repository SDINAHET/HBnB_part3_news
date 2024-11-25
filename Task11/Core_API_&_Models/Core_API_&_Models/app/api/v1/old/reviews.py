# Routes for reviews.
from flask import Blueprint, jsonify, request
from app.models import db, Review

# Crée un blueprint pour les routes des avis
bp = Blueprint('reviews', __name__)

@bp.route('/', methods=['GET'])
def get_reviews():
    """
    Récupère tous les avis.

    Returns:
        Response: Liste des avis au format JSON.
    """
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

@bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """
    Récupère un avis par son ID.

    Args:
        review_id (int): Identifiant de l'avis.

    Returns:
        Response: Détails de l'avis au format JSON.
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_review():
    """
    Crée un nouvel avis.

    Returns:
        Response: Détails de l'avis créé au format JSON.
    """
    data = request.get_json()
    if not data or 'text' not in data or 'rating' not in data or 'user_id' not in data or 'place_id' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if not (1 <= data['rating'] <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_review = Review(
        text=data['text'],
        rating=data['rating'],
        user_id=data['user_id'],
        place_id=data['place_id']
    )

    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Met à jour les informations d'un avis.

    Args:
        review_id (int): Identifiant de l'avis.

    Returns:
        Response: Détails de l'avis mis à jour au format JSON.
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()
    if 'text' in data:
        review.text = data['text']
    if 'rating' in data:
        if not (1 <= data['rating'] <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
        review.rating = data['rating']

    db.session.commit()
    return jsonify(review.to_dict()), 200

@bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Supprime un avis.

    Args:
        review_id (int): Identifiant de l'avis.

    Returns:
        Response: Confirmation de suppression.
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted"}), 200
