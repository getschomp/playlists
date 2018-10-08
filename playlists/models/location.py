from pybald.db import models


class Location(models.Model):
    def __init__(self, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)

    city = models.Column(models.Unicode(80))
    state = models.Column(models.Unicode(2))
