"""
Persistence package for handling database operations.

This package provides classes and utilities to abstract database
interactions and support CRUD operations.
"""

from .repository import SQLAlchemyRepository

__all__ = ["SQLAlchemyRepository"]
