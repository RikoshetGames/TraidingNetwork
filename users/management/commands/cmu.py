from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='ilyalew@mail.com',
            first_name='Moder',
            last_name='Moderov',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password('645595715abcd')
        user.save()
