# playlists

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

## Migrations and Seeding

Run the migrations

```bash
alembic upgrade head
```

Seed the database, by running the cli app (will require options eventually)

```bash
python playlists/cli.py
```

## Serve

Serve the application

```bash
python playlists/app.py serve
```
