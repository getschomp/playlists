import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from pybald.db import models


class Playlist(models.Model):
    def __init__(self, *args, **kwargs):
        super(Playlist, self).__init__(*args, **kwargs)

    def __repr__(self):
        return (
            f'<Playlist(id:{self.id}, location_id: {self.location_id} '
            f'start_date:{self.start_date}, end_date: {self.end_date})>'
        )
    location_id = models.Column(
        models.Integer,
        models.ForeignKey('locations.id'),
        index=True,
        nullable=True,
    )
    start_date = models.Column(models.Date())
    end_date = models.Column(models.Date())
    url = models.Column(models.Unicode(100))
