# Routes for places.
from flask import Blueprint, jsonify, request
from app.models import db, Place

# Crée un blueprint pour les routes des lieux
bp = Blueprint('places', __name__)

@bp.route('/', methods=['GET'])
def get_places():
    """
    Récupère tous les lieux.

    Returns:
        Response: Liste des lieux au format JSON.
    """
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places]), 200

@bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    """
    Récupère un lieu par son ID.

    Args:
        place_id (int): Identifiant du lieu.

    Returns:
        Response: Détails du lieu au format JSON.
    """
    place = Place.query.get(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_place():
    """
    Crée un nouveau lieu.

    Returns:
        Response: Détails du lieu créé au format JSON.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'latitude' not in data or 'longitude' not in data or 'owner_id' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_place = Place(
        name=data['name'],
        description=data.get('description'),
        latitude=data['latitude'],
        longitude=data['longitude'],
        owner_id=data['owner_id']
    )

    db.session.add(new_place)
    db.session.commit()
    return jsonify(new_place.to_dict()), 201

@bp.route('/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    """
    Met à jour les informations d'un lieu.

    Args:
        place_id (int): Identifiant du lieu.

    Returns:
        Response: Détails du lieu mis à jour au format JSON.
    """
    place = Place.query.get(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404

    data = request.get_json()
    if 'name' in data:
        place.name = data['name']
    if 'description' in data:
        place.description = data['description']
    if 'latitude' in data:
        place.latitude = data['latitude']
    if 'longitude' in data:
        place.longitude = data['longitude']
    if 'owner_id' in data:
        place.owner_id = data['owner_id']

    db.session.commit()
    return jsonify(place.to_dict()), 200

@bp.route('/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    """
    Supprime un lieu.

    Args:
        place_id (int): Identifiant du lieu.

    Returns:
        Response: Confirmation de suppression.
    """
    place = Place.query.get(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404

    db.session.delete(place)
    db.session.commit()
    return jsonify({"message": "Place deleted"}), 200
