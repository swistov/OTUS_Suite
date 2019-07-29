from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from user.models import OtusUser

from faker import Faker


class Command(BaseCommand):

    def generate(self, amount=10):
        fake = Faker(locale='ru_RU')
        for i in range(amount):
            user = fake.profile(fields=None, sex=None)
            OtusUser.objects.create(
                user=(
                    User.objects.create_user(
                        username=user['username'],
                        first_name=user['name'].split(' ')[1],
                        last_name=user['name'].split(' ')[0],
                        email=user['mail'],
                        password=fake.password(),
                        is_superuser=False,
                        is_staff=False,
                    )
                ),
                phone=fake.phone_number()
            )

    def handle(self, *args, **kwargs):
        self.generate()
