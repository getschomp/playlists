import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.orm import joinedload

from playlists.models.location import Location
from playlists.models.playlist import Playlist
from playlists.models.playlist_user import PlaylistUser
from playlists.models.user import User

locations = []

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
        global locations
        if not locations:
            locations = LocationResource.get_query(info)().all()
        return [
            location
            for location in locations
            if location.id == self.location_id
        ][0]


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
        query = PlaylistResource.get_query(info)()
        query = query.options(joinedload('location'))
        return query.all()


class Query(graphene.ObjectType):
    users = graphene.List(UserResource)

    playlists = graphene.List(PlaylistResource, id=graphene.Int())
    playlist = graphene.Field(PlaylistResource, id=graphene.Int())

    playlist_users = graphene.List(PlaylistUserResource)
    playlist_user = graphene.Field(PlaylistUserResource, id=graphene.Int())

    def resolve_users(self, info):
        query = UserResource.get_query(info)()
        return query.all()

    def resolve_playlists(self, info, id):
        query = PlaylistResource.get_query(info)()
        query = query.options(joinedload('location'))
        if id:
            query = query.get(id)
        return query.all()

    def resolve_playlist_users(self, info):
        query = PlaylistUserResource.get_query(info)()
        return query.all()

    def resolve_playlist(self, info, id):
        query = PlaylistResource.get_query(info)()
        if id:
            query = query.filter(Playlist.id == id)

        return query.first()

    def resolve_playlist_user(self, info, id):
        query = PlaylistUserResource.get_query(info)()
        if id:
            query = query.filter(PlaylistUser.id == id)
        return query.first()

schema = graphene.Schema(query=Query, types=[UserResource, PlaylistResource, PlaylistUserResource, LocationResource])
