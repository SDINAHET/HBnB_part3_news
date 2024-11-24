"""
Services package for business logic and application-specific functionalities.

This package provides the facade and other service classes to handle
business operations and communication between API routes and the database layer.
"""

from .facade import HBnBFacade

__all__ = ["HBnBFacade"]
