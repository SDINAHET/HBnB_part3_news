# Base model class definition.from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, DateTime

class BaseEntity:
    """
    Classe de base pour tous les modèles.
    Fournit des colonnes communes comme `id`, `created_at`, et `updated_at`.
    """
    @declared_attr
    def id(cls):
        """
        Colonne ID primaire unique pour chaque modèle.
        """
        return Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(cls):
        """
        Colonne pour stocker la date et l'heure de création.
        """
        return Column(DateTime, default=datetime.utcnow, nullable=False)

    @declared_attr
    def updated_at(cls):
        """
        Colonne pour stocker la date et l'heure de la dernière mise à jour.
        """
        return Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def to_dict(self):
        """
        Convertit l'objet en un dictionnaire JSON-friendly.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    def update(self, **kwargs):
        """
        Met à jour les attributs de l'instance avec les valeurs fournies.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
