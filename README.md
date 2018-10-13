# playlists

Playlists uses graphene-sqlalchemy to query data across a model of playlists, users and locations.

Graphql style queries look like 'json without the values' and allow the developer to fetch only the fields needed for a particular page.

An example query,
```
{
 users {
   username,
   firstName,
   lastName,
   playlists {
       url,
       startDate,
       endDate,
       location {
           country,
           city,
           state,
       }
   }
 }
}
```

## Setup

### Virtual Environment

Setup up poetry and python 3, system-wide.

```bash
pip install --user poetry
```

Copy .env.example to .env

```bash
cp .env.example .env
```

Create a new postgres database and use the environment variables in .env.example based on the example.

Activate poetry shell and install the dependencies

```bash
poetry shell
poetry install
```
Source the environment variables into your shell

`source .env`

All commands to follow require an activated virtual environment with environment variables sourced in the local shell.

## Migrations and Seeding

Run the migrations

```bash
alembic upgrade head
```

Seed the database, by running the cli app

```bash
python playlists/cli.py
```

## Serve

Serve the application

```bash
python playlists/app.py serve
```

Navigate to `0.0.0.0:8080/index`
