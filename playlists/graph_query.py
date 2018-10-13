import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from playlists.models.location import Location
from playlists.models.playlist import Playlist
from playlists.models.playlist_user import PlaylistUser
from playlists.models.user import User

class LocationResource(SQLAlchemyObjectType):
    class Meta:
        model = Location
        only_fields = ('city', 'state', 'country')


class PlaylistResource(SQLAlchemyObjectType):
    class Meta:
        model = Playlist
        only_fields = ('start_date', 'end_date', 'url')

    location = graphene.Field(LocationResource)

    def resolve_location(self, info):
        query = LocationResource.get_query(info)()
        return query.filter(Location.id == self.location_id).first()


class PlaylistUserResource(SQLAlchemyObjectType):
    class Meta:
        model = PlaylistUser
        only_fields = ('user_id', 'playlist_id', 'status')


class UserResource(SQLAlchemyObjectType):
    class Meta:
        model = User
        only_fields = ('username', 'first_name', 'last_name')
        exclude_fields = ('secret',)

    playlists = graphene.List(PlaylistResource)

    def resolve_playlists(self, info):
        query = PlaylistResource.get_query(info)
        return query().all()


class Query(graphene.ObjectType):
    users = graphene.List(UserResource)

    playlists = graphene.List(PlaylistResource)
    playlist = graphene.Field(PlaylistResource)

    playlist_users = graphene.List(PlaylistUserResource)
    playlist_user = graphene.Field(PlaylistUserResource)

    def resolve_users(self, info):
        query = UserResource.get_query(info)  # SQLAlchemy query
        return query().all()

    def resolve_playlists(self, info):
        query = PlaylistResource.get_query(info)  # SQLAlchemy query
        return query().all()

    def resolve_playlist_users(self, info):
        query = PlaylistUserResource.get_query(info)  # SQLAlchemy query
        return query().all()


schema = graphene.Schema(query=Query, types=[UserResource, PlaylistResource, PlaylistUserResource])
