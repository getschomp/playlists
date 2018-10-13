import random

import factory
from pybald.context import db

from playlists.models.location import Location
from playlists.models.playlist import Playlist
from playlists.models.playlist_user import PlaylistUser
from playlists.models.user import User


class PlaylistFactory(factory.Factory):
    class Meta:
        model = Playlist

    url = factory.Faker('url')
    end_date = factory.Faker('date')
    start_date = factory.Faker('date')


class LocationFactory(factory.Factory):
    class Meta:
        model = Location

    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    country = factory.Faker('country')


def seed():
    users = db.query(User).all()
    for user in users:
        num_of_playlists = random.randint(1,5)
        for count in range(0, num_of_playlists):
            location = LocationFactory.build()
            location.save(flush=True)
            playlist = PlaylistFactory.build()
            playlist.location_id = location.id
            playlist.save(flush=True)
            PlaylistUser(user_id=user.id, playlist_id=playlist.id).save(flush=True)

    db.commit()
