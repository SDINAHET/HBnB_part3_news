# Routes for users.from flask import Blueprint, jsonify, request
from app.models import db, User

# Crée un blueprint pour les routes des utilisateurs
bp = Blueprint('users', __name__)

@bp.route('/', methods=['GET'])
def get_users():
    """
    Récupère tous les utilisateurs.

    Returns:
        Response: Liste des utilisateurs au format JSON.
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Récupère un utilisateur par son ID.

    Args:
        user_id (int): Identifiant de l'utilisateur.

    Returns:
        Response: Détails de l'utilisateur au format JSON.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_user():
    """
    Crée un nouvel utilisateur.

    Returns:
        Response: Détails de l'utilisateur créé au format JSON.
    """
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(
        username=data['username'],
        email=data['email']
    )
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Met à jour les informations d'un utilisateur.

    Args:
        user_id (int): Identifiant de l'utilisateur.

    Returns:
        Response: Détails de l'utilisateur mis à jour au format JSON.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.set_password(data['password'])

    db.session.commit()
    return jsonify(user.to_dict()), 200

@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Supprime un utilisateur.

    Args:
        user_id (int): Identifiant de l'utilisateur.

    Returns:
        Response: Confirmation de suppression.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
