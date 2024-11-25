# Routes for authentication.
from flask import Blueprint, request, jsonify
from app.models import db, User
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app

# Crée un blueprint pour les routes d'authentification
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    """
    Authentifie un utilisateur et génère un token JWT.

    Returns:
        Response: Token JWT ou message d'erreur.
    """
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    # Génération du token JWT
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        },
        current_app.config['SECRET_KEY'],
        algorithm="HS256"
    )

    return jsonify({"token": token}), 200

@bp.route('/register', methods=['POST'])
def register():
    """
    Crée un nouveau compte utilisateur.

    Returns:
        Response: Détails de l'utilisateur créé ou message d'erreur.
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

@bp.route('/verify', methods=['GET'])
def verify_token():
    """
    Vérifie la validité d'un token JWT.

    Returns:
        Response: Message de confirmation ou d'erreur.
    """
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing"}), 401

    try:
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": "Token is valid", "user_id": decoded_token["user_id"]}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
