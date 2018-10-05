from pybald.db import models


class PlaylistUser(models.Model):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


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
    status = models.Column(models.Unicode(1024))
