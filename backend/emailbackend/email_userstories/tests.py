#local
import json
from email_userstories.models import Emails, User
from email_userstories.serializers import RegisterUserSerializer
#django
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

#rest-framework
from rest_framework import status
# Create your tests here.

class RegisterUserViewTest(TestCase):
    """
    Test for RegisterUserView
    """
    def setUp(self):
        """
        Initialize the data to be tested, with 2 payload one valid, another invalid.
        """
        self.client = Client()
        self.valid_payload = {
            'name': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        }
        self.invalid_payload = {
            'name': '',
            'email': '',
            'password': 'testpassword'
        }

    def test_register_valid_user(self):
        """
        This test will use a POST request in the URL with the valid payload and return 201 CREATED
        """
        response = self.client.post(
            reverse('register'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_invalid_user(self):
        """
        This test will use a POST request, and use the payload invalid returning an error 400 BAD_REQUEST
        """
        response = self.client.post(
            reverse('register'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class LoginUserViewTest(TestCase):
#     """
#     Test for LoginUserView
#     """
#     def setUp(self):
#         self.client = Client()
#         self.valid_payload = {
#             'email': 'testuser@test.com',
#             'password': 'testpassword'
#         }
#         self.invalid_payload = {
#             'email': 'wronguser@test.com',
#             'password': 'testpassword'
#         }

#     def test_login_valid_user(self):
#         self.client(email='testuser@test.com', password='testpassword')
#         response = self.client.post(
#             reverse('login'),
#             data=self.valid_payload,
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_login_invalid_user(self):
    #     response = self.client.post(
    #         reverse('login'),
    #         data=self.invalid_payload,
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_get_logged_in_user(self):
    #     self.client.login(email='testuser@test.com', password='testpassword')
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_not_logged_in_user(self):
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    


# class Send_RecieveEmailViewTest(TestCase):
#     """
#     Test for Send Email View
#     """
#     def setUp(self):
#         """
#         Make requests as a user
#         """
#         self.client = Client()
#         self.user = User.objects.create_user(email='testuser@test.com', password='testpassword')
#         self.recipient = User.objects.create_user(email='recipient@test.com', password='testpassword')
#         self.client.force_login(self.user)

#     def test_send_email_view(self):
#         """
#         Test for API

#         data: Values to post an email
#         respones: It will make a post to the 'send_email view' using the data
#         if it works will return a 201 if not it will return another status code
#         """
#         data = {
#             'recipient_email': self.recipient.email,
#             'subject': 'Test Subject',
#             'body': 'Test Body',
#         }
#         response = self.client.post(reverse('send_email'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class Recieve_EmailViewTest(TestCase):
     
#      def setUp(self):
#             self.client = Client()
#             self.email = Emails.objects.create(
#                   sender_email='remitente@example.com',
#                   recipient_email='destinatario@example.com',
#                   subject='Test Subject',
#                   body='Test Body',
#                   timestamp='2024-02-28 14:08:22' 
#             )
            
#      def test_get_email_view(self):
#         sender_email = self.email.sender_email
#         if sender_email:
#             response = self.client.get(reverse('received_email', kwargs={'sender_email': sender_email}))
#             self.assertEqual(response.status_code, 200)
#         else:
#              self.assertEqual(response.status_code, 404)