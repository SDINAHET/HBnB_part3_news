# Initialize tests package.
import pytest
from app import create_app, db

@pytest.fixture
def app():
    """
    Configure une instance de l'application Flask pour les tests.

    Returns:
        Flask: Instance de l'application Flask.
    """
    # Crée une application Flask avec la configuration de test
    app = create_app('testing')

    # Active le contexte de l'application
    with app.app_context():
        # Initialise la base de données pour les tests
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """
    Fournit un client de test pour envoyer des requêtes à l'application.

    Args:
        app (Flask): Instance de l'application Flask.

    Returns:
        FlaskClient: Client de test.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Fournit un runner de test pour exécuter des commandes CLI Flask.

    Args:
        app (Flask): Instance de l'application Flask.

    Returns:
        FlaskCliRunner: Runner CLI de test.
    """
    return app.test_cli_runner()
