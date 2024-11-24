from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Amenity

# Création d'un blueprint pour les routes administrateurs
admin_routes = Blueprint("admin_routes", __name__, url_prefix="/api/v1/admin")

# Vérification des privilèges d'administrateur
def is_admin():
    """
    Vérifie si l'utilisateur actuel est un administrateur.
    """
    current_user = get_jwt_identity()
    if not current_user.get("is_admin", False):
        return False
    return True

# Route pour créer un nouvel utilisateur
@admin_routes.route("/users", methods=["POST"])
@jwt_required()
def create_user():
    """
    Administrateur : Créer un nouvel utilisateur.
    """
    if not is_admin():
        return jsonify({"error": "Admin privileges required"}), 403

    data = request.json
    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password are required"}), 400

    # Vérification de l'unicité de l'email
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400

    new_user = User(
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", ""),
        email=data["email"],
        is_admin=data.get("is_admin", False)
    )
    new_user.hash_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": new_user.to_dict()}), 201

# Route pour modifier un utilisateur
@admin_routes.route("/users/<user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    """
    Administrateur : Modifier un utilisateur.
    """
    if not is_admin():
        return jsonify({"error": "Admin privileges required"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    # Mise à jour des données utilisateur
    if "email" in data:
        # Vérification de l'unicité de l'email
        if User.query.filter_by(email=data["email"]).first() and user.email != data["email"]:
            return jsonify({"error": "Email already in use"}), 400
        user.email = data["email"]

    if "first_name" in data:
        user.first_name = data["first_name"]

    if "last_name" in data:
        user.last_name = data["last_name"]

    if "is_admin" in data:
        user.is_admin = data["is_admin"]

    db.session.commit()

    return jsonify({"message": "User updated successfully", "user": user.to_dict()}), 200

# Route pour ajouter un nouvel équipement (amenity)
@admin_routes.route("/amenities", methods=["POST"])
@jwt_required()
def create_amenity():
    """
    Administrateur : Ajouter un nouvel équipement.
    """
    if not is_admin():
        return jsonify({"error": "Admin privileges required"}), 403

    data = request.json
    if not data.get("name"):
        return jsonify({"error": "Amenity name is required"}), 400

    # Vérification de l'unicité du nom de l'équipement
    if Amenity.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Amenity already exists"}), 400

    new_amenity = Amenity(name=data["name"])
    db.session.add(new_amenity)
    db.session.commit()

    return jsonify({"message": "Amenity created successfully", "amenity": new_amenity.to_dict()}), 201

# Route pour modifier un équipement
@admin_routes.route("/amenities/<amenity_id>", methods=["PUT"])
@jwt_required()
def update_amenity(amenity_id):
    """
    Administrateur : Modifier un équipement.
    """
    if not is_admin():
        return jsonify({"error": "Admin privileges required"}), 403

    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    data = request.json
    if "name" in data:
        # Vérification de l'unicité du nom de l'équipement
        if Amenity.query.filter_by(name=data["name"]).first() and amenity.name != data["name"]:
            return jsonify({"error": "Amenity name already exists"}), 400
        amenity.name = data["name"]

    db.session.commit()

    return jsonify({"message": "Amenity updated successfully", "amenity": amenity.to_dict()}), 200
