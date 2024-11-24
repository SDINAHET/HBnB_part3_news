from flask import Blueprint, jsonify
from models import db, Place, Review, Amenity

# Création d'un blueprint pour les routes publiques
public_routes = Blueprint("public_routes", __name__, url_prefix="/api/v1")

# Route pour obtenir tous les lieux
@public_routes.route("/places", methods=["GET"])
def get_all_places():
    """
    Obtenir la liste de tous les lieux.
    """
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places]), 200

# Route pour obtenir les détails d'un lieu
@public_routes.route("/places/<place_id>", methods=["GET"])
def get_place_by_id(place_id):
    """
    Obtenir les détails d'un lieu par ID.
    """
    place = Place.query.get(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200

# Route pour obtenir tous les avis
@public_routes.route("/reviews", methods=["GET"])
def get_all_reviews():
    """
    Obtenir la liste de tous les avis.
    """
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

# Route pour obtenir les détails d'un avis
@public_routes.route("/reviews/<review_id>", methods=["GET"])
def get_review_by_id(review_id):
    """
    Obtenir les détails d'un avis par ID.
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict()), 200

# Route pour obtenir tous les équipements (amenities)
@public_routes.route("/amenities", methods=["GET"])
def get_all_amenities():
    """
    Obtenir la liste de tous les équipements.
    """
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

# Route pour obtenir les détails d'un équipement
@public_routes.route("/amenities/<amenity_id>", methods=["GET"])
def get_amenity_by_id(amenity_id):
    """
    Obtenir les détails d'un équipement par ID.
    """
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200
