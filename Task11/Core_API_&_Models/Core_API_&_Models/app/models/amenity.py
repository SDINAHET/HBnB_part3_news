from app.models.base_entity import BaseEntity
from app import db

class Amenity(db.Model, BaseEntity):
    """
    Modèle représentant une commodité.

    Attributs :
        id (int) : Identifiant unique de la commodité (hérité de BaseEntity).
        created_at (datetime) : Timestamp de création (hérité de BaseEntity).
        updated_at (datetime) : Timestamp de dernière mise à jour (hérité de BaseEntity).
        name (str) : Nom de la commodité.
        description (str) : Description optionnelle de la commodité.
    """
    __tablename__ = 'amenities'

    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        """
        Représentation de la commodité pour le débogage.
        """
        return f"<Amenity {self.name}>"

    def to_dict(self):
        """
        Convertit la commodité en un dictionnaire JSON-friendly.

        Returns:
            dict: Dictionnaire représentant la commodité.
        """
        amenity_dict = super().to_dict()
        amenity_dict.update({
            "name": self.name,
            "description": self.description
        })
        return amenity_dict
