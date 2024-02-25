#django
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class SendEmailViewTest(TestCase):
    """
    Test for Send Email View
    """
    def setUp(self):
        """
        Make requests as a user
        """
        self.client = Client()

    def test_send_email_view_db(self):
            """
            Test for API

            data: Values to post an email
            respones: It will make a post to the 'send_email view' using the data
            if it works will return a 201 if not it will return another status code
            """
            data = {
                'recipient_email': 'test@example.com',
                'subject': 'Test Subject',
                'body': 'Test Body',
            }
            response = self.client.post(reverse('send_email'), data)
            self.assertEqual(response.status_code, 201)