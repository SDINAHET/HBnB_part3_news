Core_API_&_Models/
├── app/                        # Contient l'application Flask et ses configurations
│   ├── __init__.py             # Initialisation de l'application Flask
│   ├── config.py               # Fichier de configuration pour différents environnements
│   ├── models/                 # Contient les modèles SQLAlchemy
│   │   ├── __init__.py         # Initialisation du package des modèles
│   │   ├── base_entity.py      # Classe de base pour les modèles
│   │   ├── user.py             # Modèle pour les utilisateurs
│   │   ├── place.py            # Modèle pour les lieux
│   │   ├── review.py           # Modèle pour les avis
│   │   ├── amenity.py          # Modèle pour les commodités
│   │   └── place_amenity.py    # Table de liaison pour Place et Amenity
│   ├── api/                    # Contient les routes API
│   │   ├── __init__.py         # Initialisation du package API
│   │   ├── v1/                 # Version 1 de l'API
│   │   │   ├── __init__.py     # Initialisation des routes v1
│   │   │   ├── routes/         # Dossier pour les routes
│   │   │   │   ├── __init__.py # Initialisation des sous-routes
│   │   │   │   ├── users.py    # Routes pour les utilisateurs
│   │   │   │   ├── places.py   # Routes pour les lieux
│   │   │   │   ├── reviews.py  # Routes pour les avis
│   │   │   │   ├── amenities.py# Routes pour les commodités
│   │   │   │   └── auth.py     # Routes pour l'authentification
│   │   └── tests/              # Tests pour les endpoints
│   │       ├── __init__.py     # Initialisation du package de tests
│   │       ├── test_users.py   # Tests unitaires pour les utilisateurs
│   │       ├── test_places.py  # Tests unitaires pour les lieux
│   │       ├── test_reviews.py # Tests unitaires pour les avis
│   │       └── test_amenities.py # Tests unitaires pour les commodités
├── instance/                   # Fichiers spécifiques à l'environnement
│   ├── config.py               # Configuration locale
│   └── development.db          # Base de données SQLite pour le développement
├── migrations/                 # Scripts pour les migrations de base de données
│   ├── versions/               # Versions des migrations
│   └── env.py                  # Fichier de configuration Alembic
├── requirements.txt            # Dépendances Python
├── run.py                      # Fichier principal pour démarrer l'application
└── README.md                   # Documentation principale du projet
