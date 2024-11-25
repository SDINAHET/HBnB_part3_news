import os

# Structure des dossiers et fichiers
structure = {
    "Core_API_&_Models": {
        "app": {
            "__init__.py": "",
            "config.py": "# Configuration file for Flask environments.",
            "models": {
                "__init__.py": "# Initialize the models package.",
                "base_entity.py": "# Base model class definition.",
                "user.py": "# User model definition.",
                "place.py": "# Place model definition.",
                "review.py": "# Review model definition.",
                "amenity.py": "# Amenity model definition.",
                "place_amenity.py": "# Relationship table for Place and Amenity."
            },
            "api": {
                "__init__.py": "# Initialize the API package.",
                "v1": {
                    "__init__.py": "# Initialize API v1 routes.",
                    "routes": {
                        "__init__.py": "# Initialize sub-routes.",
                        "users.py": "# Routes for users.",
                        "places.py": "# Routes for places.",
                        "reviews.py": "# Routes for reviews.",
                        "amenities.py": "# Routes for amenities.",
                        "auth.py": "# Routes for authentication."
                    }
                },
                "tests": {
                    "__init__.py": "# Initialize tests package.",
                    "test_users.py": "# Unit tests for user endpoints.",
                    "test_places.py": "# Unit tests for place endpoints.",
                    "test_reviews.py": "# Unit tests for review endpoints.",
                    "test_amenities.py": "# Unit tests for amenity endpoints."
                }
            }
        },
        "instance": {
            "config.py": "# Local configuration.",
            "development.db": ""  # Empty SQLite database for development.
        },
        "migrations": {
            "versions": {},  # Empty directory for migration versions.
            "env.py": "# Alembic configuration file."
        },
        "requirements.txt": "# Python dependencies.",
        "run.py": "# Entry point for running the Flask application.",
        "README.md": "# Main documentation for the project."
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If content is a dict, create a folder
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create sub-structure
        else:  # Otherwise, create a file with content
            with open(path, "w") as file:
                file.write(content)

# Chemin de base
base_path = "Core_API_&_Models"

# Création de la structure
create_structure(base_path, structure)

print(f"La structure des fichiers et dossiers a été créée sous le dossier '{base_path}'.")
