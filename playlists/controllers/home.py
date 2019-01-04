import json

from pybald.context import db
from pybald.core.controllers import Controller, action

from playlists.graph_query import schema


class HomeController(Controller):

    @action
    def index(self, req):
        '''Execute Arbitrary graphql queries with

        Example Query:
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

        Example http Request:
        GET http://localhost:8080/index?query={users{username,firstName,lastName,playlists{url,startDate,endDate,location{country,city,state}}}}
        '''
        result = schema.execute(req.GET.get('query'), context_value={'session': db.connection})
        return json.dumps(result.data)
