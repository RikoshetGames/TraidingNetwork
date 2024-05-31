from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='почта',
            first_name='имя',
            last_name='фамилия',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password('password')
        user.save()
