# User model definition.from app.models.base_entity import BaseEntity
from app import db

class User(db.Model, BaseEntity):
    """
    Modèle représentant un utilisateur.

    Attributs :
        id (int) : Identifiant unique de l'utilisateur (hérité de BaseEntity).
        created_at (datetime) : Timestamp de création (hérité de BaseEntity).
        updated_at (datetime) : Timestamp de dernière mise à jour (hérité de BaseEntity).
        username (str) : Nom d'utilisateur unique.
        email (str) : Adresse e-mail unique.
        password_hash (str) : Hash du mot de passe de l'utilisateur.
    """
    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        """
        Représentation de l'utilisateur pour le débogage.
        """
        return f"<User {self.username}>"

    def to_dict(self):
        """
        Convertit l'utilisateur en un dictionnaire JSON-friendly.

        Returns:
            dict: Dictionnaire représentant l'utilisateur.
        """
        user_dict = super().to_dict()
        user_dict.update({
            "username": self.username,
            "email": self.email
        })
        return user_dict

    def set_password(self, password):
        """
        Hash le mot de passe et le stocke.

        Args:
            password (str): Mot de passe en clair.
        """
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Vérifie si le mot de passe en clair correspond au hash stocké.

        Args:
            password (str): Mot de passe en clair.

        Returns:
            bool: True si le mot de passe est correct, False sinon.
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
