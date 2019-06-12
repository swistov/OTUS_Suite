from django.contrib.auth.models import User
from django.db import models

from app_teacher.models import Teacher


class Curse(models.Model):

    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    date_time_release = models.DateTimeField()
    enabled = models.BooleanField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({"" if self.enabled else "not "}enabled)'


class Lesson(models.Model):

    name = models.CharField(max_length=100)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    descriptions = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    date_time_release = models.DateTimeField()
    enabled = models.BooleanField()

    @property
    def curse_name(self):
        return self.curse.name

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
