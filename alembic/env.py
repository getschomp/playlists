from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import pybald

pybald.bootstrap('alembic/pybald_app.py')
from pybald.context import config as pybald_config

from pybald.db import models


target_metadata = models.Base.metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(alembic_config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = target_metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

from alembic.config import Config
alembic_config = Config()
alembic_config.set_main_option("script_location", "alembic")
alembic_config.set_main_option("revision_environment", "true")
alembic_config.set_main_option("sqlalchemy.url", pybald_config.database_engine_uri.replace('%', '%%'))
alembic_config.set_section_option("alembic:exclude", "tables", "")
alembic_config.set_section_option("loggers", "keys", "root,sqlalchemy,alembic")
alembic_config.set_section_option("handlers", "keys", "console")
alembic_config.set_section_option("formatters", "keys", "generic")
alembic_config.set_section_option("logger_root", "level", "WARN")
alembic_config.set_section_option("logger_root", "handlers", "console")
alembic_config.set_section_option("logger_root", "qualname", "")
alembic_config.set_section_option("logger_sqlalchemy", "level", "WARN")
alembic_config.set_section_option("logger_sqlalchemy", "handlers", "")
alembic_config.set_section_option("logger_sqlalchemy", "qualname", "sqlalchemy.engine")
alembic_config.set_section_option("logger_alembic", "level", "INFO")
alembic_config.set_section_option("logger_alembic", "handlers", "")
alembic_config.set_section_option("logger_alembic", "qualname", "alembic")
alembic_config.set_section_option("handler_console", "class", "StreamHandler")
alembic_config.set_section_option("handler_console", "args", "(sys.stderr,)")
alembic_config.set_section_option("handler_console", "level", "NOTSET")
alembic_config.set_section_option("handler_console", "formatter", "generic")
alembic_config.set_section_option("formatter_generic", "format", "{levelname}-5.5s [{name}s] {message}s")
alembic_config.set_section_option("formatter_generic", "datefmt", "{H}:{M}:{S}")



def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
