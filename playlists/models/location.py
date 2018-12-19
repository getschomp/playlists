from pybald.db import models
from sqlalchemy.orm import backref, relationship


class Location(models.Model):
    def __init__(self, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)

    city = models.Column(models.Unicode(80))
    state = models.Column(models.Unicode(2))
    country = models.Column(models.Unicode(128))
    playlist = relationship(
        'Playlist',
        back_populates='location',
        lazy='bulk'
    )
