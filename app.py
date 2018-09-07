import pybald
from pybald import context, default_config
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

from custom_config import config_overrides

config = {**default_config, **config_overrides}

# configure our pybald application
pybald.configure(config_object=config)

def map(urls):
    urls.connect('home', r'/', controller='home')

class HomeController(Controller):
    @action
    def index(self, req):
        return "Hello!"

app = Router(routes=map, controllers=[HomeController])

if __name__ == "__main__":
    context.start(app)
