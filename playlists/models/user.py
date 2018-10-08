import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from pybald.db import models


class User(models.Model):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    username = models.Column(models.Unicode(1024))
    first_name = models.Column(models.Unicode(1024))
    last_name = models.Column(models.Unicode(1024))


class UserResource(SQLAlchemyObjectType):
    class Meta:
        model = User
        only_fields = ('username', 'first_name',)
        exclude_fields = ('last_name',)


class Query(graphene.ObjectType):
    users = graphene.List(UserResource)

    def resolve_users(self, info):
        query = UserResource.get_query(info)  # SQLAlchemy query
        return query().all()


user_schema = graphene.Schema(query=Query)
