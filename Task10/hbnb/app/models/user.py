from app import db, bcrypt
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import validates
import re


# class User(BaseModel):
class User(db.Model):
    """
    User model for HBnB system.

    Attributes:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): Email address of the user, must be unique.
        password (str): Hashed password of the user.
        is_admin (bool): Indicates if the user has administrative privileges.
        places (relationship): Relationship to the Place model.
        reviews (relationship): Relationship to the Review model.
    """
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    places = relationship('Place', back_populates='owner', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='user', cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        """
        Initialize a User instance, with optional password hashing.

        Args:
            **kwargs: Keyword arguments for initializing user fields.
        """
        super().__init__(**kwargs)
        if 'password' in kwargs:
            self.hash_password(kwargs['password'])

    def hash_password(self, password):
        """
        Hash the password before storing it.
        Args:
            password (str): Plain-text password to hash.
        """
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Verify a plain-text password against the stored hashed password.
        Args:
            password (str): Plain-text password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return bcrypt.check_password_hash(self.password, password)

    @validates('email')
    def validate_email(self, key, email):
        """
        Validate the format of an email address.

        Args:
            key (str): The name of the field being validated.
            email (str): The email address to validate.

        Returns:
            str: The validated email address.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            raise ValueError("Invalid email format.")
        return email

    def __repr__(self):
        """
        String representation of the User instance.
        """
        return f"<User(id='{self.id}', email='{self.email}', is_admin={self.is_admin})>"
