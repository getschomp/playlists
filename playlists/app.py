import pybald
from pybald import context
from pybald.core.router import Router

from custom_config import full_config

# configure pybald application
pybald.configure(config_object=full_config)

# These imports need to come after configuration
from playlists.controllers.home import HomeController


def map(urls):
    urls.connect('index', r'/index', controller='home')


app = Router(routes=map, controllers=[HomeController])


if __name__ == "__main__":
    context.start(app)
