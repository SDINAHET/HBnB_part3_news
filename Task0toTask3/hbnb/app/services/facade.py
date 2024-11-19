# Facade layer implementation
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    """
    HBnBFacade serves as the business logic layer, connecting the API and persistence layers.
    It contains methods to perform operations related to Users, Places, Reviews, and Amenities.
    """
    def __init__(self):
        # Initialize repositories for different entities
        self.user_repository = InMemoryRepository()
        self.place_repository = InMemoryRepository()
        self.review_repository = InMemoryRepository()
        self.amenity_repository = InMemoryRepository()

    # User-related operations
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def update_user(self, user_id, user_data):
        self.user_repository.update(user_id, user_data)
        return self.get_user(user_id)

    # Place-related operations
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repository.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, place_data):
        self.place_repository.update(place_id, place_data)
        return self.get_place(place_id)

    # Review-related operations
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repository.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def update_review(self, review_id, review_data):
        self.review_repository.update(review_id, review_data)
        return self.get_review(review_id)

    # Amenity-related operations
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repository.update(amenity_id, amenity_data)
        return self.get_amenity(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()
