from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Event


class EventTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        mock_date = '2021-03-04 11:57:11.703055+00:00'
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date

            testuser1 = User.objects.create_user(
                username='testuser1',
                password='pass123'
            )
            testuser1.save()

            test_event = Event.objects.create(
                author=testuser1,
                name='Test event',
                description='Test text',
                type='1',
                started_at='2021-05-05 12:20:10.703055+00:00'
            )
            test_event.save()

    def test_event_content(self):
        mock_date = '2021-03-04 11:57:11.703055+00:00'
        event = Event.objects.get(id=1)
        author = f'{event.author}'
        name = f'{event.name}'
        description = f'{event.description}'
        type = f'{event.type}'
        created_at = f'{event.created_at}'
        started_at = f'{event.started_at}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(name, 'Test event')
        self.assertEqual(description, 'Test text')
        self.assertEqual(type, '1')
        self.assertEqual(created_at, mock_date)
        self.assertEqual(started_at, '2021-05-05 12:20:10.703055+00:00')
