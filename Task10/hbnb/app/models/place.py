from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship


# class Place(BaseModel):
class Place(db.Model):
    """
    Place model to represent accommodations in the HBnB system.

    Attributes:
        title (str): The title of the place.
        description (str): A detailed description of the place.
        price (float): The price per night for staying at the place.
        latitude (float): The latitude of the place's location.
        longitude (float): The longitude of the place's location.
        owner_id (str): Foreign key referencing the owner (User) of the place.
        owner (relationship): Relationship to the User model.
        reviews (relationship): Relationship to the Review model.
        amenities (relationship): Relationship to the Amenity model through a many-to-many association.
    """
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)


    # Relationships
    owner = relationship('User', back_populates='places')
    reviews = relationship('Review', back_populates='place', cascade="all, delete-orphan")
    amenities = db.relationship(
        'Amenity',
        secondary='place_amenity',
        back_populates='places',
        lazy='subquery'
    )

    def __repr__(self):
        return f"<Place(id='{self.id}', title='{self.title}', owner_id='{self.owner_id}', price={self.price})>"
