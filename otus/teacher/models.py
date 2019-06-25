from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True)

    @property
    def first_name(self):
        return self.user.first_name

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user.last_name if self.user.last_name else self.user.username} {self.user.first_name}'
