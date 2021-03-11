from django.test import TestCase, Client

# Create your tests here.
from users.models import CustomUser


class AuthTest(TestCase):
    fixtures = [
        "fixtures/user_fixtures.json",
        "fixtures/event_fixtures.json"
    ]

    endpoints = [
        '/',
        '/users/me/',
        '/users/me/edit/',
        '/events/',
        '/events/new/',
        '/events/1/',
        '/events/1/give/',
    ]

    def test_no_auth(self):
        """User should be redirected when not logged in."""
        c = Client()

        for endpoint in self.endpoints:
            response = c.get(endpoint)
            self.assertTrue('/users/login' in response.url)

    def test_auth(self):

        """User should be guaranteed access to page when logged in."""
        c = Client()
        c.login(username='user0@test.com', password='password0')

        for endpoint in self.endpoints[:-2]:
            response = c.get(endpoint)
            self.assertEqual(200, response.status_code)
