from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

from app_main.models import Curse


class ReservedCurse(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE, related_name='user_curse')
    reserved_date_time = models.DateTimeField(auto_now_add=datetime.now)

    @property
    def curse_name(self):
        return self.curse.name

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user} reserved curse "{self.curse.name}"'
