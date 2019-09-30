from django.db import models
from user.models import Teacher, OtusUser


class Curse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField()
    teachers = models.ManyToManyField(Teacher, related_name='teachers')
    students = models.ManyToManyField(OtusUser, related_name='students', blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    date_time_release = models.DateTimeField()
    enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({"" if self.enabled else "not "}enabled)'


class Lesson(models.Model):
    name = models.CharField(max_length=100, unique=True)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    descriptions = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=1, related_name='lesson_teacher')
    add_date = models.DateTimeField(auto_now_add=True)
    date_time_release = models.DateTimeField()
    enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):

    CURRENIES = (
        ('usd', 'usd'),
        ('eur', 'eur')
    )

    currency = models.CharField(max_length=3, choices=CURRENIES)
    rate = models.DecimalField(max_digits=10, decimal_places=6, default=1)

    def __str__(self):
        return f'{self.currency} ({self.rate})'

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                rate = CurrencyRate.objects.get(currency=self.currency)
                self.pk = rate.pk
            except CurrencyRate.DoesNotExist:
                return 'Currency not exists'

        super().save(*args, **kwargs)
