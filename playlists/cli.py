import pybald
from pybald import context, default_config

from custom_config import full_config

# Cli is it's own pybald context/app with the database config
pybald.configure(config_object=full_config)

from playlists.tasks.seeds import users
from playlists.tasks.seeds import playlists

if __name__ == "__main__":
    users.seed()
    playlists.seed()
