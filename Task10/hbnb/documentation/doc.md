root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB/Part3
_HBnB_Auth_&_DB/hbnb/instance# sqlite3 development.db

-- Table: users
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,           -- Identifiant unique
    first_name TEXT NOT NULL,      -- Prénom
    last_name TEXT NOT NULL,       -- Nom
    email TEXT UNIQUE NOT NULL,    -- Email unique
    password TEXT NOT NULL,        -- Mot de passe
    is_admin BOOLEAN DEFAULT 0,    -- Statut admin (par défaut : non)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de création
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Date de mise à jour
);

-- Table: amenities
CREATE TABLE IF NOT EXISTS amenities (
    id TEXT PRIMARY KEY,           -- Identifiant unique
    name TEXT NOT NULL UNIQUE,     -- Nom unique de l'amenity
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de création
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Date de mise à jour
);

-- Table: places
CREATE TABLE IF NOT EXISTS places (
    id TEXT PRIMARY KEY,           -- Identifiant unique
    title TEXT NOT NULL,           -- Titre du lieu
    description TEXT,              -- Description
    price REAL NOT NULL,           -- Prix par nuit
    latitude REAL NOT NULL,        -- Latitude
    longitude REAL NOT NULL,       -- Longitude
    owner_id TEXT NOT NULL,        -- Référence à l'utilisateur (propriétaire)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de création
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de mise à jour
    FOREIGN KEY (owner_id) REFERENCES users (id)   -- Relation avec la table users
);

-- Table: reviews
CREATE TABLE IF NOT EXISTS reviews (
    id TEXT PRIMARY KEY,           -- Identifiant unique
    text TEXT NOT NULL,            -- Texte de l'avis
    rating INTEGER NOT NULL,       -- Note (1-5)
    user_id TEXT NOT NULL,         -- Référence à l'utilisateur (auteur de l'avis)
    place_id TEXT NOT NULL,        -- Référence au lieu (avis sur ce lieu)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de création
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date de mise à jour
    FOREIGN KEY (user_id) REFERENCES users (id),   -- Relation avec la table users
    FOREIGN KEY (place_id) REFERENCES places (id), -- Relation avec la table places
    UNIQUE (user_id, place_id)     -- Empêche les avis en double pour un même lieu
);

-- Table intermédiaire: place_amenities (relation N:N entre places et amenities)
CREATE TABLE IF NOT EXISTS place_amenities (
    place_id TEXT NOT NULL,        -- Référence au lieu
    amenity_id TEXT NOT NULL,      -- Référence à l'amenity
    FOREIGN KEY (place_id) REFERENCES places (id), -- Relation avec la table places
    FOREIGN KEY (amenity_id) REFERENCES amenities (id), -- Relation avec la table amenities
    PRIMARY KEY (place_id, amenity_id) -- Clé primaire composite pour éviter les doublons
);





-- Ajout d'un utilisateur
INSERT INTO users (id, first_name, last_name, email, password) VALUES
('user1', 'John', 'Doe', 'john.doe@example.com', 'securepassword');

-- Ajout d'un amenity
INSERT INTO amenities (id, name) VALUES
('amenity1', 'Wi-Fi');

-- Ajout d'un lieu
INSERT INTO places (id, title, price, latitude, longitude, owner_id) VALUES
('place1', 'Cozy Apartment', 75.0, 48.8566, 2.3522, 'user1');

-- Ajout d'un avis
INSERT INTO reviews (id, text, rating, user_id, place_id) VALUES
('review1', 'Great stay!', 5, 'user1', 'place1');

-- Ajout d'une relation entre place et amenity
INSERT INTO place_amenities (place_id, amenity_id) VALUES
('place1', 'amenity1');



SELECT * FROM users;
SELECT * FROM amenities;
SELECT * FROM places;
SELECT * FROM reviews;
SELECT * FROM place_amenities;

Flask==2.1.3
flask-restx==0.5.1
marshmallow==3.18.0
requests==2.31.0
flask-bcrypt==1.0.1
flask-jwt-extended==4.4.4
pytest==7.3.1
sqlalchemy==1.4.47
flask-sqlalchemy==2.5.1
Werkzeug==2.1.2
pytest
pytest-flask
pytest-cov

```textplain

hbnb/
├── app/
│   ├── __init__.py                # Initialisation principale de Flask
│   ├── api/
│   │   ├── __init__.py            # Initialisation pour les namespaces API
│   │   └── v1/                    # Version 1 des routes API
│   │       ├── __init__.py        # Initialisation des routes versionnées
│   │       ├── amenities.py       # Routes pour gérer les Amenities
│   │       ├── auth.py            # Authentification (JWT)
│   │       ├── places.py          # Routes pour gérer les Places
│   │       ├── protected.py       # Routes protégées pour tests
│   │       ├── reviews.py         # Routes pour gérer les Reviews
│   │       └── users.py           # Routes pour gérer les Users (incl. admin)
│   ├── models/
│   │   ├── __init__.py            # Initialisation du module des modèles
│   │   ├── amenity.py             # Modèle SQLAlchemy pour les Amenities
│   │   ├── base_entity.py         # Classe de base commune (BaseModel)
│   │   ├── place.py               # Modèle SQLAlchemy pour les Places
│   │   ├── review.py              # Modèle SQLAlchemy pour les Reviews
│   │   └── user.py                # Modèle SQLAlchemy pour les Users
│   ├── services/
│   │   ├── __init__.py            # Initialisation du module de services
│   │   ├── facade.py              # Facade pour les services CRUD
│   │   └── repositories/
│   │       ├── __init__.py        # Initialisation des repositories
│   │       ├── amenity_repository.py # Repository SQLAlchemy pour les Amenities
│   │       ├── base_repository.py    # Classe Repository générique
│   │       ├── place_repository.py  # Repository SQLAlchemy pour les Places
│   │       ├── review_repository.py # Repository SQLAlchemy pour les Reviews
│   │       └── user_repository.py   # Repository SQLAlchemy pour les Users
│   ├── utils/
│   │   ├── __init__.py            # Initialisation des utilitaires
│   │   ├── validators.py          # Validation des données (regex, etc.)
│   │   └── jwt_helpers.py         # Fonctions d'aide pour JWT
│   ├── config.py                  # Configuration Flask (dev/prod/test)
│   └── db/
│       ├── create_schema.sql      # Script SQL pour la génération de la base
│       └── seed_data.sql          # Script SQL pour insérer des données initiales
├── instance/
│   └── development.db             # Base SQLite pour le développement
├── migrations/                    # Gestion des migrations (Flask-Migrate)
│   ├── alembic.ini                # Fichier de configuration Alembic
│   ├── env.py                     # Environnement de migration
│   ├── README                     # Documentation des migrations
│   ├── script.py.mako             # Modèle pour les scripts de migration
│   └── versions/                  # Dossiers pour les versions migrées
├── tests/                         # Tests unitaires et d'intégration
│   ├── __init__.py                # Initialisation des tests
│   ├── integration/
│   │   ├── __init__.py            # Tests d'intégration API
│   │   ├── test_auth.py           # Tests sur l'authentification JWT
│   │   ├── test_places.py         # Tests intégrés sur les Places
│   │   ├── test_reviews.py        # Tests intégrés sur les Reviews
│   │   └── test_users.py          # Tests intégrés sur les Users
│   └── unit/
│       ├── __init__.py            # Tests unitaires sur les utilitaires
│       ├── test_validators.py     # Tests unitaires des validateurs
│       └── test_repositories.py   # Tests unitaires des repositories
├── requirements.txt               # Dépendances Python
├── .env                           # Variables d'environnement (Flask_SECRET_KEY, etc.)
├── run.py                         # Fichier pour démarrer l'application
└── README.md                      # Documentation principale du projet
```

hbnb/
├── api/
│   ├── __init__.py
│   ├── v1/
│   │   ├── __init__.py
│   │   ├── places.py
│   │   ├── reviews.py
│   │   ├── amenities.py
│   │   ├── users.py
│   │   ├── auth.py
│   │   ├── routes/
│   │   │   ├── admin_routes.py
│   │   │   ├── public_routes.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── place.py
│   ├── review.py
│   ├── amenity.py
├── migrations/
│   ├── versions/
│   ├── alembic.ini
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_places.py
│   ├── test_reviews.py
├── requirements.txt
├── config.py
├── run.py
├── .env (non inclus dans l'archive finale)
├── README.md



hbnb/
│
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── routes/
│   │       │   ├── __init__.py
│   │       │   └── auth.py
│   │       ├── users.py
│   │       ├── places.py
│   │       └── reviews.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   │   └── repository.py
│   └── config.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_places.py
│   └── test_reviews.py
│
├── migrations/
│   ├── versions/
│   └── env.py
├── requirements.txt
├── run.py
└── README.md


hbnb/
├── alembic/                  # Gestion des migrations de base de données
│   ├── versions/             # Dossiers contenant les versions de migration
│   ├── env.py                # Configuration des migrations Alembic
│   ├── script.py.mako        # Template de script pour Alembic
│   └── alembic.ini           # Configuration principale d'Alembic
│
├── app/                      # Contient l'application Flask principale
│   ├── __init__.py           # Initialisation de l'application Flask
│   ├── api/                  # Gestion des routes API
│   │   ├── __init__.py       # Initialisation des routes API
│   │   ├── v1/               # Version 1 de l'API
│   │   │   ├── __init__.py   # Initialisation de l'API v1
│   │   │   ├── routes/       # Organisation des routes API
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py   # Routes liées à l'authentification
│   │   │   │   ├── users.py  # Routes liées aux utilisateurs
│   │   │   │   ├── places.py # Routes liées aux lieux
│   │   │   │   ├── reviews.py # Routes liées aux avis
│   │   │   │   └── amenities.py # Routes liées aux commodités
│   │   │   └── admin_routes.py  # Routes réservées aux administrateurs
│   │
│   ├── models/               # Contient les modèles SQLAlchemy
│   │   ├── __init__.py       # Initialisation des modèles
│   │   ├── base_model.py     # Modèle de base avec les attributs communs
│   │   ├── user.py           # Modèle pour les utilisateurs
│   │   ├── place.py          # Modèle pour les lieux
│   │   ├── review.py         # Modèle pour les avis
│   │   ├── amenity.py        # Modèle pour les commodités
│   │   └── place_amenity.py  # Table d'association pour lieu/commodités
│   │
│   ├── services/             # Contient les services (Business Logic)
│   │   ├── __init__.py       # Initialisation des services
│   │   ├── facade.py         # Service principal de l'application
│   │   └── repository/       # Repositories pour interaction DB
│   │       ├── __init__.py   # Initialisation des repositories
│   │       ├── repository.py # Repository générique SQLAlchemy
│   │       └── user_repository.py # Repository pour les utilisateurs
│
│   ├── static/               # Fichiers statiques pour le frontend (si applicable)
│   │   ├── css/              # Fichiers CSS
│   │   └── js/               # Fichiers JavaScript
│
│   ├── templates/            # Templates Jinja2 pour le rendu HTML (si applicable)
│   │   └── index.html
│
│   └── config.py             # Fichier de configuration pour Flask
│
├── instance/                 # Fichiers spécifiques à l'environnement (e.g., dev.db)
│   ├── development.db        # Base de données SQLite (pour développement)
│   └── config.py             # Configuration spécifique à l'instance
│
├── migrations/               # Gestion des migrations de base de données (Alembic)
│
├── tests/                    # Contient tous les tests automatisés
│   ├── __init__.py           # Initialisation des tests
│   ├── test_auth.py          # Tests pour les endpoints d'authentification
│   ├── test_users.py         # Tests pour les endpoints utilisateurs
│   ├── test_places.py        # Tests pour les endpoints lieux
│   ├── test_reviews.py       # Tests pour les endpoints avis
│   └── test_amenities.py     # Tests pour les endpoints commodités
│
├── run.py                    # Script pour démarrer le serveur Flask
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation principale du projet
└── .env                      # Variables d'environnement (ex. JWT secret, DB URI)


hbnb/
├── app/
│   ├── __init__.py         # App initialization and configuration
│   ├── api/
│   │   ├── __init__.py     # API versioning setup
│   │   ├── v1/
│   │   │   ├── __init__.py # V1 namespace
│   │   │   ├── routes/
│   │   │   │   ├── auth.py          # Authentication routes
│   │   │   │   ├── users.py         # User management routes
│   │   │   │   ├── places.py        # Place routes
│   │   │   │   ├── reviews.py       # Review routes
│   │   │   │   ├── amenities.py     # Amenity routes
│   │   │   │   └── admin_routes.py  # Admin-specific routes
│   ├── models/
│   │   ├── __init__.py      # Model registration
│   │   ├── base_model.py    # BaseModel with shared functionality
│   │   ├── user.py          # User model
│   │   ├── place.py         # Place model
│   │   ├── review.py        # Review model
│   │   ├── amenity.py       # Amenity model
│   │   └── place_amenity.py # Many-to-many relation
│   ├── services/
│   │   ├── __init__.py      # Services initialization
│   │   ├── facade.py        # Core logic for handling API operations
│   └── persistence/
│       ├── __init__.py      # Persistence layer initialization
│       └── repository.py    # SQLAlchemy repository for data handling
├── instance/
│   ├── development.db       # Development database (SQLite)
│   └── config.py            # Configuration overrides for dev/production
├── migrations/
│   ├── versions/            # Alembic migration scripts
│   ├── env.py               # Alembic configuration for migrations
│   ├── script.py.mako       # Alembic template
├── tests/
│   ├── __init__.py          # Test initialization
│   ├── test_auth.py         # Tests for authentication routes
│   ├── test_users.py        # Tests for user routes
│   ├── test_places.py       # Tests for places routes
│   ├── test_reviews.py      # Tests for reviews routes
│   ├── test_amenities.py    # Tests for amenities routes
├── run.py                   # Entry point for running the Flask app
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignored files

---

### **Split into Parts**
#### **Part 1: Core App**
- `app/` (without models)
- `run.py`
- `README.md`

#### **Part 2: Models**
- `app/models/`

#### **Part 3: Routes**
- `app/api/`

#### **Part 4: Services**
- `app/services/`
- `app/persistence/`

#### **Part 5: Migrations**
- `migrations/`

#### **Part 6: Tests**
- `tests/`

#### **Part 7: Configuration & Instance**
- `instance/`
- `requirements.txt`

---

Let me know if this organization works for you!


hbnb/
├── alembic/                  # Gestion des migrations de la base de données
│   ├── versions/             # Historique des migrations
│   ├── env.py                # Configuration pour les migrations
│   └── alembic.ini           # Fichier de configuration Alembic
├── app/                      # Dossier principal contenant l'application Flask
│   ├── __init__.py           # Initialisation de l'application Flask
│   ├── api/                  # Routes de l'API
│   │   ├── __init__.py       # Initialisation des routes API
│   │   └── v1/               # Version 1 de l'API
│   │       ├── __init__.py   # Initialisation de l'API V1
│   │       ├── auth.py       # Routes d'authentification (connexion, inscription)
│   │       ├── users.py      # Routes pour les utilisateurs
│   │       ├── places.py     # Routes pour les places
│   │       ├── reviews.py    # Routes pour les reviews
│   │       ├── amenities.py  # Routes pour les amenities
│   │       └── protected.py  # Routes protégées nécessitant une authentification
│   ├── models/               # Modèles SQLAlchemy
│   │   ├── __init__.py       # Initialisation des modèles
│   │   ├── base_model.py     # Classe de base pour tous les modèles
│   │   ├── user.py           # Modèle User
│   │   ├── place.py          # Modèle Place
│   │   ├── review.py         # Modèle Review
│   │   ├── amenity.py        # Modèle Amenity
│   │   └── place_amenity.py  # Modèle de liaison Place-Amenity
│   ├── services/             # Logique métier et services
│   │   ├── __init__.py       # Initialisation des services
│   │   └── facade.py         # Service principal pour centraliser les interactions
│   ├── persistence/          # Gestion de la persistance et des repositories
│   │   ├── __init__.py       # Initialisation de la persistance
│   │   └── repository.py     # Repositories pour accéder aux données
│   ├── tests/                # Tests unitaires et d'intégration
│   │   ├── __init__.py       # Initialisation des tests
│   │   ├── test_auth.py      # Tests pour l'authentification
│   │   ├── test_users.py     # Tests pour les utilisateurs
│   │   ├── test_places.py    # Tests pour les places
│   │   ├── test_reviews.py   # Tests pour les reviews
│   │   ├── test_amenities.py # Tests pour les amenities
│   │   └── test_endpoints.py # Tests d'intégration de tous les endpoints
├── migrations/               # Fichiers générés automatiquement par Flask-Migrate
│   ├── versions/             # Historique des migrations
│   └── alembic.ini           # Configuration de Flask-Migrate
├── instance/                 # Fichiers spécifiques à l'environnement
│   ├── config.py             # Configuration locale (développement)
│   └── development.db        # Base de données SQLite pour le développement
├── scripts/                  # Scripts utilitaires
│   ├── generate_schema.sql   # Script SQL pour générer le schéma de la BDD
│   └── populate_data.sql     # Script SQL pour insérer les données initiales
├── requirements.txt          # Liste des dépendances Python
├── run.py                    # Script principal pour démarrer l'application Flask
├── config.py                 # Configuration globale
├── README.md                 # Documentation du projet
└── .env                      # Variables d'environnement (non incluses dans le dépôt)



hbnb/
├── alembic/                # Dossier pour la gestion des migrations de la base de données
│   ├── env.py              # Script principal pour Alembic
│   ├── script.py.mako      # Modèle pour les scripts de migration
│   └── versions/           # Dossier contenant les versions des migrations
├── app/                    # Contient l'application Flask
│   ├── __init__.py         # Initialisation de l'application
│   ├── api/                # Contient les endpoints (routes)
│   │   ├── __init__.py     # Initialisation des routes
│   │   └── v1/             # Version 1 de l'API
│   │       ├── __init__.py # Initialisation des routes de l'API v1
│   │       ├── auth.py     # Routes pour l'authentification
│   │       ├── users.py    # Routes pour les utilisateurs
│   │       ├── places.py   # Routes pour les places
│   │       ├── reviews.py  # Routes pour les reviews
│   │       ├── amenities.py# Routes pour les amenities
│   │       ├── admin.py    # Routes pour les fonctions administrateur
│   ├── models/             # Contient les modèles SQLAlchemy
│   │   ├── __init__.py     # Initialisation des modèles
│   │   ├── base_model.py   # Modèle de base pour les entités
│   │   ├── user.py         # Modèle pour les utilisateurs
│   │   ├── place.py        # Modèle pour les places
│   │   ├── amenity.py      # Modèle pour les amenities
│   │   ├── review.py       # Modèle pour les reviews
│   │   ├── place_amenity.py# Modèle de liaison Place-Amenity
│   ├── services/           # Contient la logique métier
│   │   ├── __init__.py     # Initialisation des services
│   │   └── facade.py       # Interface pour accéder à la logique métier
│   ├── utils/              # Contient des fonctions utilitaires
│   │   ├── validators.py   # Validateurs pour les entrées utilisateur
│   │   └── helpers.py      # Fonctions auxiliaires
├── instance/               # Fichiers spécifiques à l'environnement
│   ├── config.py           # Configuration pour Flask (développement et production)
│   ├── development.db      # Base de données SQLite pour le développement
├── tests/                  # Contient tous les tests unitaires et d'intégration
│   ├── test_users.py       # Tests pour les utilisateurs
│   ├── test_places.py      # Tests pour les places
│   ├── test_reviews.py     # Tests pour les reviews
│   ├── test_amenities.py   # Tests pour les amenities
│   ├── test_auth.py        # Tests pour l'authentification
├── migrations/             # Gestion des migrations avec Alembic
├── run.py                  # Point d'entrée principal pour démarrer le serveur Flask
├── requirements.txt        # Liste des dépendances Python nécessaires
└── README.md               # Documentation du projet


Détails des Fichiers et Dossiers
1. Alembic
alembic/env.py : Définit la configuration de base d'Alembic.
alembic/versions/ : Contient les fichiers de migration.
2. App
app/__init__.py : Configure l'application Flask et initialise les extensions.
app/api/ : Contient les endpoints (API RESTful) pour l'application.
auth.py : Routes pour l'authentification (connexion, déconnexion).
users.py : Routes pour gérer les utilisateurs (CRUD).
places.py : Routes pour les lieux.
reviews.py : Routes pour les avis (reviews).
amenities.py : Routes pour les commodités (amenities).
admin.py : Routes réservées aux administrateurs.
app/models/ : Définit les modèles SQLAlchemy.
base_model.py : Modèle de base avec des champs communs (id, created_at, updated_at).
user.py : Modèle pour les utilisateurs (ex. : email, password, is_admin).
place.py : Modèle pour les lieux (places).
review.py : Modèle pour les avis.
amenity.py : Modèle pour les commodités.
place_amenity.py : Table intermédiaire pour les relations Place - Amenity.
app/services/ : Contient la logique métier.
facade.py : Point d'entrée pour toutes les opérations complexes.
app/utils/ : Contient les fonctions auxiliaires (ex. : validation des emails).
3. Instance
config.py : Configuration de l'application Flask (clé secrète, base de données).
development.db : Base de données SQLite (environnement de développement).
4. Tests
Tests unitaires et d'intégration pour valider les fonctionnalités :
test_users.py : Tests pour les utilisateurs.
test_places.py : Tests pour les lieux.
test_reviews.py : Tests pour les avis.
test_amenities.py : Tests pour les commodités.
test_auth.py : Tests pour les endpoints d'authentification.
Démarrer le Projet
Installation
Cloner le dépôt :
bash
Copier le code
git clone https://github.com/username/hbnb.git
cd hbnb
Installer les dépendances :
bash
Copier le code
pip install -r requirements.txt
Configuration
Modifier instance/config.py pour adapter à votre environnement.
Base de Données
Initialiser la base de données (avec Alembic) :
bash
Copier le code
flask db upgrade
Lancer le Serveur
Démarrer le serveur Flask :
bash
Copier le code
python run.py
Documentation API
Swagger : Documentation complète accessible via http://localhost:5000/swagger/.
