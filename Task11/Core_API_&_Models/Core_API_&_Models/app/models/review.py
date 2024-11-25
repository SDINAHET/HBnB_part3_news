from app.models.base_entity import BaseEntity
from app import db

class Review(db.Model, BaseEntity):
    """
    Modèle représentant un avis.

    Attributs :
        id (int) : Identifiant unique de l'avis (hérité de BaseEntity).
        created_at (datetime) : Timestamp de création (hérité de BaseEntity).
        updated_at (datetime) : Timestamp de dernière mise à jour (hérité de BaseEntity).
        text (str) : Contenu de l'avis.
        rating (int) : Note attribuée (1 à 5).
        user_id (int) : Référence à l'utilisateur ayant laissé l'avis.
        place_id (int) : Référence au lieu auquel l'avis est associé.
    """
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)

    # Relations
    user = db.relationship('User', backref=db.backref('reviews', lazy='dynamic'))
    place = db.relationship('Place', backref=db.backref('reviews', lazy='dynamic'))

    def __repr__(self):
        """
        Représentation de l'avis pour le débogage.
        """
        return f"<Review {self.id} - Rating: {self.rating}>"

    def to_dict(self):
        """
        Convertit l'avis en un dictionnaire JSON-friendly.

        Returns:
            dict: Dictionnaire représentant l'avis.
        """
        review_dict = super().to_dict()
        review_dict.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        return review_dict
