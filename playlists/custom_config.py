import os

pg_username = os.environ['PG_USERNAME']
pg_password = os.environ['PG_PASSWORD']
pg_host = os.environ['PG_HOST']
pg_port = os.environ['PG_PORT']
database_name = os.environ['DATABASE_NAME']

DATABASE_URL = (
    f'postgresql://{pg_username}'
    f':{pg_password}@{pg_host}:{pg_port}/{database_name}'
)

config_overrides = dict(
    database_engine_uri=DATABASE_URL,
)
