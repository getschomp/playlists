import logging
from pybald.db import models


class Playlist(models.Model):

    def __init__(self, *args, **kargs):
        super(Playlist, self).__init__(*args, **kwargs)

    def __repr__(self):
        return (
            f'<Playlist(id:{self.id}, city:{self.city}, state:{self.state}, '
            f'start_date:{self.start_date}, end_date{self.end_date})>'
        )

    city = models.Column(models.Unicode(80), index=True, key='username')
    state = models.Column(models.Unicode(1024))
    start_date = models.Column(models.Unicode(1024))
    end_date = models.Column(models.Unicode(1024))
    # timestamped model?
