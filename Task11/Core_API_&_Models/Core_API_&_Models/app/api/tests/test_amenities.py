# Unit tests for amenity endpoints.
import pytest
from app.models import db, Amenity

def test_get_all_amenities(client):
    """
    Teste la récupération de toutes les commodités.
    """
    # Ajouter des commodités fictives dans la base de données
    amenity1 = Amenity(name="WiFi")
    amenity2 = Amenity(name="Parking")
    db.session.add_all([amenity1, amenity2])
    db.session.commit()

    response = client.get('/api/v1/amenities/')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_amenity_by_id(client):
    """
    Teste la récupération d'une commodité par son ID.
    """
    amenity = Amenity(name="Swimming Pool")
    db.session.add(amenity)
    db.session.commit()

    response = client.get(f'/api/v1/amenities/{amenity.id}')
    assert response.status_code == 200
    assert response.json['name'] == "Swimming Pool"

def test_get_amenity_not_found(client):
    """
    Teste le cas où une commodité n'existe pas.
    """
    response = client.get('/api/v1/amenities/999')
    assert response.status_code == 404
    assert response.json['error'] == "Amenity not found"

def test_create_amenity(client):
    """
    Teste la création d'une nouvelle commodité.
    """
    data = {
        "name": "Gym",
        "description": "Fully equipped fitness center"
    }
    response = client.post('/api/v1/amenities/', json=data)
    assert response.status_code == 201
    assert response.json['name'] == "Gym"

def test_create_amenity_missing_fields(client):
    """
    Teste la création d'une commodité avec des champs manquants.
    """
    data = {}
    response = client.post('/api/v1/amenities/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Missing required fields"

def test_create_amenity_duplicate_name(client):
    """
    Teste la création d'une commodité avec un nom déjà existant.
    """
    amenity = Amenity(name="Duplicate Amenity")
    db.session.add(amenity)
    db.session.commit()

    data = {
        "name": "Duplicate Amenity"
    }
    response = client.post('/api/v1/amenities/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Amenity already exists"

def test_update_amenity(client):
    """
    Teste la mise à jour d'une commodité existante.
    """
    amenity = Amenity(name="Old Amenity")
    db.session.add(amenity)
    db.session.commit()

    data = {
        "name": "Updated Amenity",
        "description": "Updated description"
    }
    response = client.put(f'/api/v1/amenities/{amenity.id}', json=data)
    assert response.status_code == 200
    assert response.json['name'] == "Updated Amenity"
    assert response.json['description'] == "Updated description"

def test_update_amenity_not_found(client):
    """
    Teste la mise à jour d'une commodité inexistante.
    """
    data = {
        "name": "Non-existent Amenity"
    }
    response = client.put('/api/v1/amenities/999', json=data)
    assert response.status_code == 404
    assert response.json['error'] == "Amenity not found"

def test_delete_amenity(client):
    """
    Teste la suppression d'une commodité.
    """
    amenity = Amenity(name="Delete Amenity")
    db.session.add(amenity)
    db.session.commit()

    response = client.delete(f'/api/v1/amenities/{amenity.id}')
    assert response.status_code == 200
    assert response.json['message'] == "Amenity deleted"

    # Vérifie que la commodité a été supprimée
    deleted_amenity = Amenity.query.get(amenity.id)
    assert deleted_amenity is None

def test_delete_amenity_not_found(client):
    """
    Teste la suppression d'une commodité inexistante.
    """
    response = client.delete('/api/v1/amenities/999')
    assert response.status_code == 404
    assert response.json['error'] == "Amenity not found"
