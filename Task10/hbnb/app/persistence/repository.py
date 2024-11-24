from app import db
from sqlalchemy.exc import SQLAlchemyError

class SQLAlchemyRepository:
    """
    A generic repository class for SQLAlchemy models.
    Provides common CRUD operations for any SQLAlchemy model.
    """
    def __init__(self, model):
        """
        Initialize the repository with a specific SQLAlchemy model.

        Args:
            model (db.Model): The SQLAlchemy model to manage.
        """
        self.model = model

    def add(self, obj):
        """
        Add a new object to the database session and commit.

        Args:
            obj (db.Model): The object to add to the database.
        """
        try:
            db.session.add(obj)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error adding object: {e}")

    def get(self, obj_id):
        """
        Retrieve an object by its primary key.

        Args:
            obj_id (str): The primary key of the object to retrieve.

        Returns:
            db.Model: The retrieved object, or None if not found.
        """
        return self.model.query.get(obj_id)

    def get_all(self):
        """
        Retrieve all objects of the model.

        Returns:
            list: A list of all objects of the model.
        """
        return self.model.query.all()

    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object by a specific attribute.

        Args:
            attr_name (str): The attribute name to filter by.
            attr_value (any): The value of the attribute to filter by.

        Returns:
            db.Model: The first object that matches the filter, or None if not found.
        """
        return self.model.query.filter_by(**{attr_name: attr_value}).first()

    def update(self, obj_id, updates):
        """
        Update an existing object in the database.

        Args:
            obj_id (str): The primary key of the object to update.
            updates (dict): A dictionary of attribute updates.

        Returns:
            db.Model: The updated object.
        """
        obj = self.get(obj_id)
        if not obj:
            raise ValueError(f"Object with ID {obj_id} not found.")

        try:
            for key, value in updates.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()
            return obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error updating object: {e}")

    def delete(self, obj_id):
        """
        Delete an object from the database.

        Args:
            obj_id (str): The primary key of the object to delete.
        """
        obj = self.get(obj_id)
        if not obj:
            raise ValueError(f"Object with ID {obj_id} not found.")

        try:
            db.session.delete(obj)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error deleting object: {e}")

    def filter_by(self, **filters):
        """
        Retrieve all objects that match the given filters.

        Args:
            filters (dict): A dictionary of attribute-value filters.

        Returns:
            list: A list of objects that match the filters.
        """
        return self.model.query.filter_by(**filters).all()

    def query_custom(self, query):
        """
        Execute a custom query on the model.

        Args:
            query (sqlalchemy.orm.Query): A SQLAlchemy query object.

        Returns:
            list: The result of the query.
        """
        try:
            return query.all()
        except SQLAlchemyError as e:
            raise ValueError(f"Error executing custom query: {e}")
