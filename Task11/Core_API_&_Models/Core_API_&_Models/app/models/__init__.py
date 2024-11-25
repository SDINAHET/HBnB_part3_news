# Initialize the models package.from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'instance SQLAlchemy
db = SQLAlchemy()

# Importation des modèles pour qu'ils soient enregistrés avec SQLAlchemy
from app.models.base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenity

def init_app(app):
    """
    Initialise les modèles avec l'application Flask.

    Args:
        app (Flask): Instance de l'application Flask.
    """
    db.init_app(app)

    # Crée toutes les tables dans la base de données si elles n'existent pas déjà
    with app.app_context():
        db.create_all()
