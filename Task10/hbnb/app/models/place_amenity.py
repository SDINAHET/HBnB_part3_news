from app import db

# Association table for many-to-many relationship between Place and Amenity
place_amenity = db.Table(
    'place_amenity',
    db.Column(
        'place_id',
        db.String(36),
        db.ForeignKey('places.id', ondelete="CASCADE"),
        primary_key=True
    ),
    db.Column(
        'amenity_id',
        db.String(36),
        db.ForeignKey('amenities.id', ondelete="CASCADE"),
        primary_key=True
    )
)