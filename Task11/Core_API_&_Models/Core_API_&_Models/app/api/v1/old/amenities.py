# Routes for amenities.
from flask import Blueprint, jsonify, request
from app.models import db, Amenity

# Crée un blueprint pour les routes des commodités
bp = Blueprint('amenities', __name__)

@bp.route('/', methods=['GET'])
def get_amenities():
    """
    Récupère toutes les commodités.

    Returns:
        Response: Liste des commodités au format JSON.
    """
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@bp.route('/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
    Récupère une commodité par son ID.

    Args:
        amenity_id (int): Identifiant de la commodité.

    Returns:
        Response: Détails de la commodité au format JSON.
    """
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_amenity():
    """
    Crée une nouvelle commodité.

    Returns:
        Response: Détails de la commodité créée au format JSON.
    """
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if Amenity.query.filter_by(name=data['name']).first():
        return jsonify({"error": "Amenity already exists"}), 400

    new_amenity = Amenity(
        name=data['name'],
        description=data.get('description')
    )

    db.session.add(new_amenity)
    db.session.commit()
    return jsonify(new_amenity.to_dict()), 201

@bp.route('/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """
    Met à jour les informations d'une commodité.

    Args:
        amenity_id (int): Identifiant de la commodité.

    Returns:
        Response: Détails de la commodité mise à jour au format JSON.
    """
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    data = request.get_json()
    if 'name' in data:
        amenity.name = data['name']
    if 'description' in data:
        amenity.description = data['description']

    db.session.commit()
    return jsonify(amenity.to_dict()), 200

@bp.route('/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Supprime une commodité.

    Args:
        amenity_id (int): Identifiant de la commodité.

    Returns:
        Response: Confirmation de suppression.
    """
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    db.session.delete(amenity)
    db.session.commit()
    return jsonify({"message": "Amenity deleted"}), 200
