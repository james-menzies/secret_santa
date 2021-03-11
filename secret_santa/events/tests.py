from datetime import timedelta

from django.template import Template
from django.test import TestCase, Client

from events.models import Event, Gift


# Create your tests here.
def verify_template(desired_template: str,
                    returned_templates: Template) -> bool:
    template_strings = [template.name for template in returned_templates]
    return desired_template in template_strings


class EventTest(TestCase):
    fixtures = [
        "fixtures/user_fixtures.json",
        "fixtures/event_fixtures.json"
    ]

    def setUp(self) -> None:
        self.c1 = Client()
        self.c2 = Client()

        self.c1.login(
            username='user1@test.com',
            password='password1'
        )

        self.c2.login(
            username='user9@test.com',
            password='password9'
        )

    def test_auth(self):
        """Users should only be able to access events that they are part of"""

        response = self.c1.get('/')

        self.assertEqual(200, response.status_code)

        response = self.c2.get('/events/6/')
        self.assertEqual(302, response.status_code)

    def test_progression(self):
        response = self.c1.get('/events/6/')
        self.assertTrue(verify_template('events/event_view_inactive.html', response.templates))
        response = self.c1.get('/events/6/activate/', follow=True)

        self.assertEqual(response.redirect_chain[0][0], '/events/6/')
        event = Event.objects.prefetch_related('gifts').get(pk=6)

        # concluded at and activated at should now be present on event object
        self.assertIsNotNone(event.concluded_at)
        self.assertIsNotNone(event.activated_at)

        # should be 5 gift objects associated with event now.
        self.assertEqual(5, len(event.gifts.all()))

        # verify new template is returned
        self.assertTrue(verify_template('events/event_view_active.html',
                                        response.templates))

        # modify event conclusion
        event.concluded_at -= timedelta(days=1)
        event.save()

        # event should now be concluded
        response = self.c1.get('/events/6/')
        self.assertTrue(verify_template('events/event_view_opening.html', response.templates))

        # on reload, event should render reveal template
        response = self.c1.get('/events/6/')
        self.assertTrue(verify_template('events/event_view_reveal.html', response.templates))
