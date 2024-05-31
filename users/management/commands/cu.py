from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user1 = User.objects.create(
            email='почта',
            first_name='имя',
            last_name='фамилия',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user1.set_password('password')
        user1.save()

        user2 = User.objects.create(
            email='test2@gmail.com',
            first_name='Tester2',
            last_name='Testerov',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user2.set_password('password')
        user2.save()
