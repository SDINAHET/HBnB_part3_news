# from app import create_app

# app = create_app()

# with app.app_context():
#     # Crée toutes les tables définies dans vos modèles
#     db.create_all()
#     print("Base de données initialisée : development.db")

# if __name__ == "__main__":
#     app.run(debug=True)

#!/usr/bin/python3
from app import create_app

# Crée l'application Flask
app = create_app()

if __name__ == "__main__":
    # Démarre le serveur Flask en mode débogage
    app.run(debug=True, host="0.0.0.0", port=5000)
