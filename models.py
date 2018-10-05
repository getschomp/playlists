import logging
from pybald.db import models


class Playlist(models.Model):

    def __init__(self, *args, **kwargs):
        super(Playlist, self).__init__(*args, **kwargs)

    def __repr__(self):
        return (
            f'<Playlist(id:{self.id}, city:{self.city}, state:{self.state}, '
            f'start_date:{self.start_date}, end_date{self.end_date})>'
        )

    location_id = models.Column('location_id', models.Integer, models.ForeignKey("location.id"))
    start_date = models.Column(models.Unicode(1024))
    end_date = models.Column(models.Unicode(1024))


class Location(models.Model):

    def __init__(self, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)

    city = models.Column(models.Unicode(80))
    state = models.Column(models.Unicode(2))


class UserPlaylist(models.Model):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    user_id = models.Column(models.Unicode(1024))
    playlist_id = models.Column(models.Unicode(1024))
    status = models.Column(models.Unicode(1024))


class User(models.Model):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    username = models.Column(models.Unicode(1024))
    first_name = models.Column(models.Unicode(1024))
    last_name = models.Column(models.Unicode(1024))
