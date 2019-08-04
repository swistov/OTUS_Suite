from django.db import models
from django.contrib.auth.models import User


class OtusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otus_user')
    phone = models.CharField(max_length=11)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}' or f'{self.user.username}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user.last_name if self.user.last_name else self.user.username} {self.user.first_name}'
