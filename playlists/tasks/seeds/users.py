from pybald.context import db

from playlists.models.user import User


def seed():
    users = [
        dict(username='candybam182', first_name='Jim', last_name='Bean'),
        dict(username='swimmer88', first_name='Joe', last_name='Willikers'),
        dict(username='therealjohnsmith', first_name='John', last_name='Smith'),
    ]
    for user in users:
        user = User(**user)
        user.save()
    db.flush()
    db.commit()
