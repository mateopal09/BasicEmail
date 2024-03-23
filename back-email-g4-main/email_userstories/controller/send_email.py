#Backend
from ..models import Emails
from ..serializers import EmailSendSerializer
from ..services.service_send_email import service_send_email

#django
from django.contrib.auth import get_user_model


#rest-framework
from rest_framework import status, generics
from rest_framework.response import Response


class SendEmailView(generics.CreateAPIView):
    """
    Send Email

    This view handles the process of sending an email. It accepts a POST request containing the recipient's email, 
    subject, and body of the email, validates these inputs, and then creates a new email in the database.

    Attributes
        - serializer_class: The serializer class that this view will use to validate and deserialize input, 
          and to serialize output.

    Methods
        - create(request, *args, **kwargs): Handles a POST request. It retrieves the sender from the session, 
          the recipient, subject, and body from the request data, creates a new email with these data, and then 
          saves the new email to the database.
    """
    serializer_class = EmailSendSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles a POST request to send email.

        Parameters
            - request: The request that triggered this method. The request.data should contain the recipient's email, 
              subject, and body of the email.

        Returns
            - A Response object with a message indicating the success of the email sending process, and a status code 
              indicating the success of the operation. If the operation was successful, the status code will be 201 CREATED.
        """
        try:
            data = service_send_email(request)
            #Validate if user session is ongoing 
            return Response({'detail': ' Email sent succesfully'}, status=status.HTTP_201_CREATED)
        except (Exception):
            if Exception == "No user logged in":
                return Response({"detail":"No user logged in. Please log in to send an email."},status=status.HTTP_400_BAD_REQUEST)
            elif  Exception == "Sender not logged in":
                return Response({"detail":"Sender not logged in"}, status=status.HTTP_404_NOT_FOUND)
            elif Exception == "Recipient email is required":
                return Response({"detail":"Recipient email is required."}, status=status.HTTP_400_BAD_REQUEST)
            elif Exception == "Recipient not found":
                return Response({"detail":"Recipient not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(f'Error: {Exception}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)