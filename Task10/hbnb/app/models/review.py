from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship


# class Review(BaseModel):
class Review(db.Model):
    """
    Review model to represent reviews for places in the HBnB system.

    Attributes:
        text (str): The content of the review.
        rating (int): The rating of the review (1-5).
        user_id (str): Foreign key referencing the user who wrote the review.
        place_id (str): Foreign key referencing the place being reviewed.
        user (relationship): Relationship to the User model.
        place (relationship): Relationship to the Place model.
    """
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    def __repr__(self):
        return f"<Review(id='{self.id}', user_id='{self.user_id}', place_id='{self.place_id}', rating={self.rating})>"
