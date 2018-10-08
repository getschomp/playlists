import pybald
from pybald import context, default_config

from playlists.custom_config import config_overrides

config = {**default_config, **config_overrides}

# configure pybald application
pybald.configure(config_object=config)

from playlists.seeds import users

if __name__ == "__main__":
    users.seed()
