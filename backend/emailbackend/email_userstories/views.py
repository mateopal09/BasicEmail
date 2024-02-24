from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Emails
from .serializers import EmailSerializer
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
