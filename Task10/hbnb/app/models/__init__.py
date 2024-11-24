from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Import models to ensure they are registered with SQLAlchemy
from .base_model import BaseModel
from .user import User
from .place import Place
from .review import Review
from .amenity import Amenity
from .place_amenity import PlaceAmenity

__all__ = [
    "BaseModel",
    "User",
    "Place",
    "Review",
    "Amenity",
    "PlaceAmenity",
]
