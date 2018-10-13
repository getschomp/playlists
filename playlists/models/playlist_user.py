import graphene
from sqlalchemy.orm import backref, relationship
from pybald.db import models

from playlists.models.playlist import Playlist
from playlists.models.user import User


class PlaylistUser(models.Model):
    def __init__(self, *args, **kwargs):
        super(PlaylistUser, self).__init__(*args, **kwargs)

    user_id = models.Column(
        models.Integer,
        models.ForeignKey('users.id'),
        index=True
    )
    playlist_id = models.Column(
        models.Integer,
        models.ForeignKey('playlists.id'),
        index=True
    )
    playlist = relationship(Playlist, backref=backref('playlist'), single_parent=True, cascade="all, delete-orphan")
    user = relationship(User, backref=backref('user'), single_parent=True, cascade="all, delete-orphan")
    status = models.Column(models.Unicode(1024))
