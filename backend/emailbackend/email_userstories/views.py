from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Emails
from .serializers import EmailSerializer, EmailRecieveSerializer
# Create your views here.

class SendEmailView(APIView):
    """
    Send Email View

    This class will send an Email

    Methods.
    - Post (self, request, format=None).
    """
    def post(self, request, format=None):
        """
        Post

        Parameters:
        - request: It will have the data to send
        - format=None: Django will determine the format of input data

        This will save an instance of the serializer for the data request it
        Then if serializer has a data it will save it, and with a status code 200
        If not it will return 400 status code
        """
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class RecievedEmailView(APIView):
    """
    Email Recieved View

    This class received an email sent

    Methods get
    """

    def get(self,request, sender_email, format=None):
        """
        get

        Parameters: 
        - request: Don't use it for now, just for convention
        - sender_email: Email of the sender
        - format=None: Django will determine the format of the input data

        This will look for the email of the sender, input with sender_email.
        Then if it exists, It will go for the model and look for the information,
        If it exists, will return the information, if not will return 404 status code with description.
        
        """
        emails = Emails.objects.filter(sender_email=sender_email)
        if emails:
            serializer = EmailRecieveSerializer(emails, many=True)
            return Response(serializer.data)
        return Response({"detail": "No emails found for this sender"}, status=status.HTTP_404_NOT_FOUND)