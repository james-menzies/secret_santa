import os

from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Ensures that superuser exists in db.'
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    def handle(self, *args, **options):
        print("Checking if superuser is present")
        if not CustomUser.objects.filter(email=self.email).exists():
            CustomUser.objects.create_superuser(self.email, self.password)
        else:
            print("Superuser already present.")
