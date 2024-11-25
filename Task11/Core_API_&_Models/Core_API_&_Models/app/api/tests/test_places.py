# Unit tests for place endpoints.
import pytest
from app.models import db, Place

def test_get_all_places(client):
    """
    Teste la récupération de tous les lieux.
    """
    # Ajouter des lieux fictifs dans la base de données
    place1 = Place(name="Place 1", latitude=40.7128, longitude=-74.0060, owner_id=1)
    place2 = Place(name="Place 2", latitude=34.0522, longitude=-118.2437, owner_id=1)
    db.session.add_all([place1, place2])
    db.session.commit()

    response = client.get('/api/v1/places/')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_place_by_id(client):
    """
    Teste la récupération d'un lieu par son ID.
    """
    place = Place(name="Place Test", latitude=51.5074, longitude=-0.1278, owner_id=1)
    db.session.add(place)
    db.session.commit()

    response = client.get(f'/api/v1/places/{place.id}')
    assert response.status_code == 200
    assert response.json['name'] == "Place Test"

def test_get_place_not_found(client):
    """
    Teste le cas où un lieu n'existe pas.
    """
    response = client.get('/api/v1/places/999')
    assert response.status_code == 404
    assert response.json['error'] == "Place not found"

def test_create_place(client):
    """
    Teste la création d'un nouveau lieu.
    """
    data = {
        "name": "New Place",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "owner_id": 1
    }
    response = client.post('/api/v1/places/', json=data)
    assert response.status_code == 201
    assert response.json['name'] == "New Place"

def test_create_place_missing_fields(client):
    """
    Teste la création d'un lieu avec des champs manquants.
    """
    data = {
        "name": "Incomplete Place"
    }
    response = client.post('/api/v1/places/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Missing required fields"

def test_update_place(client):
    """
    Teste la mise à jour d'un lieu existant.
    """
    place = Place(name="Old Place", latitude=0.0, longitude=0.0, owner_id=1)
    db.session.add(place)
    db.session.commit()

    data = {
        "name": "Updated Place",
        "latitude": 48.8566,
        "longitude": 2.3522
    }
    response = client.put(f'/api/v1/places/{place.id}', json=data)
    assert response.status_code == 200
    assert response.json['name'] == "Updated Place"

def test_update_place_not_found(client):
    """
    Teste la mise à jour d'un lieu inexistant.
    """
    data = {
        "name": "Non-existent Place"
    }
    response = client.put('/api/v1/places/999', json=data)
    assert response.status_code == 404
    assert response.json['error'] == "Place not found"

def test_delete_place(client):
    """
    Teste la suppression d'un lieu.
    """
    place = Place(name="Delete Place", latitude=10.0, longitude=10.0, owner_id=1)
    db.session.add(place)
    db.session.commit()

    response = client.delete(f'/api/v1/places/{place.id}')
    assert response.status_code == 200
    assert response.json['message'] == "Place deleted"

    # Vérifie que le lieu a été supprimé
    deleted_place = Place.query.get(place.id)
    assert deleted_place is None

def test_delete_place_not_found(client):
    """
    Teste la suppression d'un lieu inexistant.
    """
    response = client.delete('/api/v1/places/999')
    assert response.status_code == 404
    assert response.json['error'] == "Place not found"
