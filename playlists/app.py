import pybald
from pybald import context
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

from custom_config import full_config

# configure pybald application
pybald.configure(config_object=full_config)

#TODO: move to controllers when extracted
from playlists.models.user import user_schema
from pybald.context import db
import json

def map(urls):
    urls.connect('home', r'/', controller='home')

class HomeController(Controller):

    @action
    def index(self, req):
        query = '''
            query {
              users {
                username,
                firstName
              }
            }
        '''
        result = user_schema.execute(query, context_value={'session': db.connection})
        return json.dumps(result.data)

app = Router(routes=map, controllers=[HomeController])

if __name__ == "__main__":
    context.start(app)
