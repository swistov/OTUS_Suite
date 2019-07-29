from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from user.models import Teacher

from faker import Faker


class Command(BaseCommand):

    def generate(self, amount=10):
        fake = Faker(locale='ru_RU')
        for i in range(amount):
            user = fake.profile(fields=None, sex=None)
            Teacher.objects.create(
                user=(
                    User.objects.create_user(
                        username=user['username'],
                        first_name=user['name'].split(' ')[0],
                        last_name=' '.join(user['name'].split(' ')[-1:]),
                        email=user['mail'],
                        password=fake.password(),
                        is_superuser=False,
                        is_staff=False,
                    )
                ),
                biography=fake.text(max_nb_chars=100, ext_word_list=None)
            )

    def handle(self, *args, **kwargs):
        self.generate()
