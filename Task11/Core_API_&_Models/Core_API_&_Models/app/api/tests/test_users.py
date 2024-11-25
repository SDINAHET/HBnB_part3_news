# Unit tests for user endpoints.
import pytest
from app.models import db, User

def test_get_all_users(client):
    """
    Teste la récupération de tous les utilisateurs.
    """
    # Ajouter des utilisateurs fictifs dans la base de données
    user1 = User(username="user1", email="user1@example.com")
    user1.set_password("password1")
    user2 = User(username="user2", email="user2@example.com")
    user2.set_password("password2")
    db.session.add_all([user1, user2])
    db.session.commit()

    # Envoyer une requête GET pour récupérer tous les utilisateurs
    response = client.get('/api/v1/users/')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_user_by_id(client):
    """
    Teste la récupération d'un utilisateur par son ID.
    """
    user = User(username="user_test", email="testuser@example.com")
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    response = client.get(f'/api/v1/users/{user.id}')
    assert response.status_code == 200
    assert response.json['username'] == "user_test"

def test_get_user_not_found(client):
    """
    Teste le cas où un utilisateur n'existe pas.
    """
    response = client.get('/api/v1/users/999')
    assert response.status_code == 404
    assert response.json['error'] == "User not found"

def test_create_user(client):
    """
    Teste la création d'un utilisateur.
    """
    data = {
        "username": "new_user",
        "email": "newuser@example.com",
        "password": "securepassword"
    }
    response = client.post('/api/v1/users/', json=data)
    assert response.status_code == 201
    assert response.json['username'] == "new_user"

def test_create_user_missing_fields(client):
    """
    Teste la création d'un utilisateur avec des champs manquants.
    """
    data = {
        "username": "incomplete_user"
    }
    response = client.post('/api/v1/users/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Missing required fields"

def test_create_user_duplicate_email(client):
    """
    Teste la création d'un utilisateur avec une adresse e-mail déjà existante.
    """
    user = User(username="existing_user", email="duplicate@example.com")
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    data = {
        "username": "new_user",
        "email": "duplicate@example.com",
        "password": "securepassword"
    }
    response = client.post('/api/v1/users/', json=data)
    assert response.status_code == 400
    assert response.json['error'] == "Email already exists"

def test_update_user(client):
    """
    Teste la mise à jour d'un utilisateur.
    """
    user = User(username="old_user", email="olduser@example.com")
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    data = {
        "username": "updated_user",
        "email": "updateduser@example.com"
    }
    response = client.put(f'/api/v1/users/{user.id}', json=data)
    assert response.status_code == 200
    assert response.json['username'] == "updated_user"

def test_delete_user(client):
    """
    Teste la suppression d'un utilisateur.
    """
    user = User(username="delete_user", email="deleteuser@example.com")
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    response = client.delete(f'/api/v1/users/{user.id}')
    assert response.status_code == 200
    assert response.json['message'] == "User deleted"

    # Vérifie que l'utilisateur est supprimé
    deleted_user = User.query.get(user.id)
    assert deleted_user is None
