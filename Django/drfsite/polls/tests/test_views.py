from rest_framework.test import APITestCase # type: ignore
from rest_framework import status # type: ignore
from polls.models import Poll, Choice

class PollTests(APITestCase):
    def setUp(self):
        # Create test data
        self.poll = Poll.objects.create(question="Test Poll", pub_date="2024-01-01T00:00:00Z")
        self.choice = Choice.objects.create(poll=self.poll, choice_text="Test Choice", votes=0)
        self.poll_url = f'/polls/{self.poll.id}/'
        self.choices_url = f'/polls/{self.poll.id}/choices/'

    def test_get_poll_list(self):
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_poll_detail(self):
        response = self.client.get(self.poll_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.poll.question)

    def test_create_choice(self):
        data = {"choice_text": "New Choice", "votes": 0}
        response = self.client.post(self.choices_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Choice.objects.count(), 2)

    def test_get_choice(self):
        response = self.client.get(f'{self.choices_url}{self.choice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.choice.choice_text)
