from django.db import models
from django.contrib.auth.models import User

from app_main.models import Curse


class ReservedCurse(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE, related_name='user_curse')
    reserved_date_time = models.DateTimeField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user} reserved curse {self.curse}'
