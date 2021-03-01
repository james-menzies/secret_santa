from django.test import TestCase

# Create your tests here.
from users.models import CustomUser


class SampleTest(TestCase):
    fixtures = ["fixtures/sample_user.json"]

    def test_user_exists(self):
        user = CustomUser.objects.get(pk=1)
        self.assertEqual("admin@admin.com", user.email)
