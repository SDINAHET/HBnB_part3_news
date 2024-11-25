# Unit tests for review endpoints.
import pytest
from app.models import db, Review

def test_get_all_reviews(client):
    """
    Teste la récupération de tous les avis.
    """
    # Ajouter des avis fictifs dans la base de données
    review1 = Review(text="Amazing place!", rating=5, user_id=1, place_id=1)
    review2 = Review(text="Not bad.", rating=3, user_id=1, place_id=2)
    db.session.add_all([review1, review2])
    db.session.commit()

    response = client.get('/api/v1/reviews/')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_review_by_id(client):
    """
    Teste la récupération d'un avis par son ID.
    """
    review = Review(text="Nice spot!", rating=4, user_id=1, place_id=1)
    db.session.add(review)
    db.session.commit()

    response = client.get(f'/api/v1/reviews/{review.id}')
    assert response.status_code == 200
    assert response.json['text'] == "Nice spot!"

def test_get_review_not_found(client):
    """
    Teste le cas où un avis n'existe pas.
    """
    response = client.get('/api/v1/reviews/999')
    assert response.status_code == 404
    assert response.json['error'] == "Review not found"

def test_create_review(client):
    """
    Teste la création d'un nouvel avis.
    """
    data = {
        "text": "Fantastic experience!",
        "rating": 5,
        "user_id": 1,
        "place_id": 1
    }
    response = client.post('/api/v1/reviews/', json=data)
    assert response.status_code == 201
    assert response.json['text'] == "Fantastic experience!"

def test_create_review_missing_fields(client):
    """
    Teste la création d'un avis avec des champs manquants.
    """
    data = {
        "text": "Incomplete review"
    }
    response = client.post('/api/v1/reviews/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Missing required fields"

def test_create_review_invalid_rating(client):
    """
    Teste la création d'un avis avec une note invalide.
    """
    data = {
        "text": "Bad rating",
        "rating": 6,  # Note invalide
        "user_id": 1,
        "place_id": 1
    }
    response = client.post('/api/v1/reviews/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Rating must be between 1 and 5"

def test_update_review(client):
    """
    Teste la mise à jour d'un avis existant.
    """
    review = Review(text="Average place", rating=3, user_id=1, place_id=1)
    db.session.add(review)
    db.session.commit()

    data = {
        "text": "Updated review",
        "rating": 4
    }
    response = client.put(f'/api/v1/reviews/{review.id}', json=data)
    assert response.status_code == 200
    assert response.json['text'] == "Updated review"
    assert response.json['rating'] == 4

def test_update_review_not_found(client):
    """
    Teste la mise à jour d'un avis inexistant.
    """
    data = {
        "text": "Non-existent review"
    }
    response = client.put('/api/v1/reviews/999', json=data)
    assert response.status_code == 404
    assert response.json['error'] == "Review not found"

def test_delete_review(client):
    """
    Teste la suppression d'un avis.
    """
    review = Review(text="To be deleted", rating=2, user_id=1, place_id=1)
    db.session.add(review)
    db.session.commit()

    response = client.delete(f'/api/v1/reviews/{review.id}')
    assert response.status_code == 200
    assert response.json['message'] == "Review deleted"

    # Vérifie que l'avis a été supprimé
    deleted_review = Review.query.get(review.id)
    assert deleted_review is None

def test_delete_review_not_found(client):
    """
    Teste la suppression d'un avis inexistant.
    """
    response = client.delete('/api/v1/reviews/999')
    assert response.status_code == 404
    assert response.json['error'] == "Review not found"
