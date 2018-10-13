import json

import pybald
from pybald import context
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

from custom_config import full_config

# configure pybald application
pybald.configure(config_object=full_config)

from playlists.graph_query import schema
from pybald.context import db

def map(urls):
    urls.connect('index', r'/index', controller='home')

class HomeController(Controller):

    @action
    def index(self, req):
        query = '''
        {
          users {
            username,
            firstName,
            lastName,
            playlists {
                url,
                startDate,
                endDate,
                location {
                    country,
                    city,
                    state,
                }
            }
          }
        }
        '''
        result = schema.execute(query, context_value={'session': db.connection})
        return json.dumps(result.data)


app = Router(routes=map, controllers=[HomeController])

if __name__ == "__main__":
    context.start(app)
