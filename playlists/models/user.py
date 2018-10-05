from pybald.db import models


class User(models.Model):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    username = models.Column(models.Unicode(1024))
    first_name = models.Column(models.Unicode(1024))
    last_name = models.Column(models.Unicode(1024))
