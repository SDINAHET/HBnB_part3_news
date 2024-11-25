# Alembic configuration file.
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app import db
from app.models import *  # Importez tous vos modèles ici pour qu'Alembic les détecte

# Cette section configure le fichier de log de Alembic
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Cible SQLAlchemy pour les modèles
target_metadata = db.metadata

def run_migrations_offline():
    """
    Exécute les migrations en mode hors ligne.
    Génère les commandes SQL à exécuter manuellement.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    Exécute les migrations en mode en ligne.
    Connecte Alembic à la base de données et applique les migrations.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
