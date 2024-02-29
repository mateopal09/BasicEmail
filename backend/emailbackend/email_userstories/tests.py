#django
from django.test import TestCase, Client
from django.urls import reverse

from email_userstories.models import Emails
# Create your tests here.

class Send_RecieveEmailViewTest(TestCase):
    """
    Test for Send Email View
    """
    def setUp(self):
        """
        Make requests as a user
        """
        self.client = Client()

    def test_send_email_view(self):
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

class Recieve_EmailViewTest(TestCase):
     
     def setUp(self):
            self.client = Client()
            self.email = Emails.objects.create(
                  sender_email='remitente@example.com',
                  recipient_email='destinatario@example.com',
                  subject='Test Subject',
                  body='Test Body',
                  timestamp='2024-02-28 14:08:22' 
            )
            
     def test_get_email_view(self):
        sender_email = self.email.sender_email
        if sender_email:
            response = self.client.get(reverse('received_email', kwargs={'sender_email': sender_email}))
            self.assertEqual(response.status_code, 200)
        else:
             self.assertEqual(response.status_code, 404)