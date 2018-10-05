"""
Boilerplate code for starting up a standalone PyBald/SQLAlchemy environment
(for command line utilities, etc.)
"""
from pybald import default_config

from playlists.custom_config import config_overrides

config = {**default_config, **config_overrides}

import pybald

context = pybald.configure(config_object=config)

from pybald.db import models

from sqlalchemy.schema import (
    Constraint,
    Index,
    UniqueConstraint,
)
from sqlalchemy import event

import playlists.models.all
