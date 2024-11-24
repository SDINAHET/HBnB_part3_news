from datetime import datetime
import uuid
from app import db

class BaseModel(db.Model):
    """
    BaseModel class that includes common fields for all models in the HBnB system.

    Attributes:
        id (str): Primary key, a unique UUID4 identifier for the object.
        created_at (datetime): Timestamp when the object is created.
        updated_at (datetime): Timestamp when the object is last updated.
    """
    __abstract__ = True  # Prevents SQLAlchemy from creating a table for this model

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """
        Save the current instance to the database.
        If the instance is new, it will be added and committed to the session.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current instance from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """
        Convert the object into a dictionary format, including only serializable fields.

        Returns:
            dict: Dictionary representation of the object.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def update(self, **kwargs):
        """
        Update the attributes of the model with the provided keyword arguments.

        Args:
            **kwargs: Key-value pairs to update on the instance.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        self.save()

    def __repr__(self):
        """
        String representation of the object for debugging purposes.

        Returns:
            str: String representation of the object.
        """
        return f"<{self.__class__.__name__} id='{self.id}'>"
