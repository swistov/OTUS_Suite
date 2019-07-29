import datetime
import random
import pytz
from django.core.management.base import BaseCommand

from faker import Faker

from main.models import Curse, Lesson
from user.models import Teacher, OtusUser


class Command(BaseCommand):

    def generate_lessons(self, curse=1, amount=10):
        """
        :param curse: curse_id
        :param amount: How many lessons create to the curse
        :return: Create lessons
        """
        self.curse = curse
        self.amount = amount

        fake = Faker(locale='ru_RU')
        curse = Curse.objects.get(pk=self.curse)

        for i in range(amount):
            Lesson.objects.create(
                name=fake.sentence(nb_words=random.randint(3, 15), variable_nb_words=True, ext_word_list=None),
                curse=curse,
                descriptions=fake.text(max_nb_chars=100, ext_word_list=None),
                teacher=Teacher.objects.get(pk=random.choice(curse.teachers.values_list('id', flat=True))),
                date_time_release=fake.date_time_between_dates(datetime_start=datetime.datetime.now(),
                                                                   tzinfo=pytz.timezone('Europe/Moscow')),
                enabled=random.choice([True, False])
            )

    def generate(self, amount=10):
        fake = Faker(locale='ru_RU')
        teachers = list(Teacher.objects.values_list('id', flat=True))
        students = list(OtusUser.objects.values_list('id', flat=True))
        for i in range(amount):
            curse = Curse.objects.create(
                name=fake.sentence(nb_words=random.randint(3, 7), variable_nb_words=True, ext_word_list=None),
                descriptions=fake.text(max_nb_chars=100, ext_word_list=None),
                date_time_release=fake.date_time_between_dates(datetime_start=datetime.datetime.now(),
                                                               tzinfo=pytz.timezone('Europe/Moscow')),
                enabled=random.choice([True, False])
            )
            curse.teachers.add(
                *random.sample(teachers, random.randint(1, len(teachers)))
            )
            curse.students.add(
                    *random.sample(students, random.randint(1, len(students)))
                )
            self.generate_lessons(curse=curse.id)

    def handle(self, *args, **kwargs):
        self.generate()
