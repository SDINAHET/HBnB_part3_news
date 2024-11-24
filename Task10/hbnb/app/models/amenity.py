from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship


# class Amenity(BaseModel):
class Amenity(db.Model):
    """
    Amenity model to represent amenities in the HBnB system.

    Attributes:
        name (str): The name of the amenity.
        places (relationship): A many-to-many relationship with the Place model.
    """
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    # Many-to-Many relationship with Place
    places = relationship(
        'Place',
        secondary='place_amenity',
        back_populates='amenities',
        lazy='dynamic'
    )

    def __repr__(self):
        return f"<Amenity(id='{self.id}', name='{self.name}')>"
