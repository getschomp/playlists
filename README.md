# playlists

Setup up poetry and python 3.

Copy .env.example to .env

```bash
cp .env.example .env
```

Setup Database and environment variables in .env.example based on the example.

Activate poetry shell and install the dependencies

```python
poetry shell
poetry install
```
Source the environment variables into your shell

`source .env`

Serve the application (in the virtural env created by poetry)

```
python playlists/app.py serve
```
