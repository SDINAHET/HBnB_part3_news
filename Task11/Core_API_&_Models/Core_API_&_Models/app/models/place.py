from app.models.base_entity import BaseEntity
from app import db

class Place(db.Model, BaseEntity):
    """
    Modèle représentant un lieu.

    Attributs :
        id (int) : Identifiant unique du lieu (hérité de BaseEntity).
        created_at (datetime) : Timestamp de création (hérité de BaseEntity).
        updated_at (datetime) : Timestamp de dernière mise à jour (hérité de BaseEntity).
        name (str) : Nom du lieu.
        description (str) : Description du lieu.
        latitude (float) : Latitude du lieu.
        longitude (float) : Longitude du lieu.
        owner_id (int) : Référence à l'identifiant de l'utilisateur propriétaire.
        amenities (list) : Liste des commodités associées au lieu (relation many-to-many).
    """
    __tablename__ = 'places'

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relation many-to-many avec Amenity
    amenities = db.relationship(
        'Amenity',
        secondary='place_amenity',
        backref=db.backref('places', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        """
        Représentation du lieu pour le débogage.
        """
        return f"<Place {self.name}>"

    def to_dict(self):
        """
        Convertit le lieu en un dictionnaire JSON-friendly.

        Returns:
            dict: Dictionnaire représentant le lieu.
        """
        place_dict = super().to_dict()
        place_dict.update({
            "name": self.name,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": [amenity.id for amenity in self.amenities]
        })
        return place_dict
