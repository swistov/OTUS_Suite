from django.db import models


class Curse(models.Model):

    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    enabled = models.BooleanField()

    def __str__(self):
        return f'{self.name} ({"" if self.enabled else "not "}enabled)'
