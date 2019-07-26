from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

# from main.models import Curse


class OtusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otus_user')
    phone = models.CharField(max_length=11)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}' or f'{self.user.username}'


class ReservedCurse(models.Model):

    user = models.OneToOneField(OtusUser, on_delete=models.CASCADE, related_name='user_name')
    # curse = models.ManyToManyField(Curse, related_name='user_curse')
    reserved_date_time = models.DateTimeField(auto_now_add=datetime.now)

    # @property
    # def curse_name(self):
    #     return self.curse.name
    #
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user} reserved curse "{self.curse.name}"'


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
