from app import db

# Table de liaison entre Place et Amenity
place_amenity = db.Table(
    'place_amenity',
    db.Column(
        'place_id',
        db.Integer,
        db.ForeignKey('places.id', ondelete="CASCADE"),
        primary_key=True
    ),
    db.Column(
        'amenity_id',
        db.Integer,
        db.ForeignKey('amenities.id', ondelete="CASCADE"),
        primary_key=True
    )
)
