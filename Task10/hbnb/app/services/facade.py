from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import uuid

class HBnBFacade:
    def __init__(self):
        # Repositories for models
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    # User-related operations
    def create_user(self, user_data):
        """Create a new user with hashed password."""
        user_data['id'] = str(uuid.uuid4())  # Generate UUID for user
        user_data['password'] = generate_password_hash(user_data['password'])
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def authenticate_user(self, email, password):
        """Authenticate user and return a JWT token."""
        user = self.user_repo.get_by_attribute('email', email)
        if user and check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return {"token": token, "user_id": user.id}
        return None

    def get_user(self, user_id):
        """Retrieve user by ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve user by email."""
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, updates):
        """Update user details, excluding sensitive fields like email or password."""
        if 'email' in updates or 'password' in updates:
            raise ValueError("You cannot update email or password directly.")
        self.user_repo.update(user_id, updates)

    # Place-related operations
    def create_place(self, place_data):
        """Create a new place and associate it with the current user."""
        place_data['id'] = str(uuid.uuid4())  # Generate UUID for place
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def update_place(self, place_id, updates, current_user_id):
        """Update a place's details, ensuring the current user owns it."""
        place = self.place_repo.get(place_id)
        if not place or place.owner_id != current_user_id:
            raise PermissionError("Unauthorized to update this place.")
        self.place_repo.update(place_id, updates)

    def delete_place(self, place_id, current_user_id):
        """Delete a place, ensuring the current user owns it."""
        place = self.place_repo.get(place_id)
        if not place or place.owner_id != current_user_id:
            raise PermissionError("Unauthorized to delete this place.")
        self.place_repo.delete(place_id)

    # Review-related operations
    def create_review(self, review_data, current_user_id):
        """Create a review for a place, ensuring the user has not reviewed it before."""
        review_data['id'] = str(uuid.uuid4())  # Generate UUID for review
        review_data['user_id'] = current_user_id
        place_id = review_data.get('place_id')

        # Validate place exists and user doesn't own it
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Invalid place ID.")
        if place.owner_id == current_user_id:
            raise ValueError("You cannot review your own place.")

        # Ensure the user hasn't already reviewed this place
        existing_review = self.review_repo.get_by_attribute('user_id', current_user_id)
        if existing_review and existing_review.place_id == place_id:
            raise ValueError("You have already reviewed this place.")

        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def update_review(self, review_id, updates, current_user_id):
        """Update a review, ensuring the user owns it."""
        review = self.review_repo.get(review_id)
        if not review or review.user_id != current_user_id:
            raise PermissionError("Unauthorized to update this review.")
        self.review_repo.update(review_id, updates)

    def delete_review(self, review_id, current_user_id):
        """Delete a review, ensuring the user owns it."""
        review = self.review_repo.get(review_id)
        if not review or review.user_id != current_user_id:
            raise PermissionError("Unauthorized to delete this review.")
        self.review_repo.delete(review_id)

    # Amenity-related operations
    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity_data['id'] = str(uuid.uuid4())  # Generate UUID for amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def update_amenity(self, amenity_id, updates):
        """Update an amenity."""
        self.amenity_repo.update(amenity_id, updates)

    def delete_amenity(self, amenity_id):
        """Delete an amenity."""
        self.amenity_repo.delete(amenity_id)
