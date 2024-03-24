#Backend
from ..models import Emails
from ..serializers import EmailRecieveSerializer

#django
from django.contrib.auth import get_user_model


#rest-framework
from rest_framework import status, generics
from rest_framework.response import Response

class RecievedEmailView(generics.ListAPIView):
    """
    Recieved Email

    This view handles the process of retrieving the emails received by the logged-in user. It accepts a GET request, 
    retrieves the user from the session, and then retrieves all emails where the recipient is the user.

    Attributes
        - serializer_class: The serializer class that this view will use to serialize output.

    Methods
        - get_queryset(): Retrieves the queryset that should be used for list views, and that should be used as the 
          base for lookups in detail views. In this case, it retrieves all emails where the recipient is the user.
    """
    serializer_class = EmailRecieveSerializer

    def list(self, request, *args, **kwargs):
        """
        Overrides the list method of the ListAPIView.

        This method is called when a GET request is made. It checks if a user is logged in. If a user is logged in, 
        it calls the list method of the superclass, otherwise it returns a 400 BAD REQUEST response.

        Parameters
            - request: The request that triggered this method.

        Returns
            - A Response object with a message indicating the success or failure of the logout process. If the logout was successful, the status code will be 200 OK. If the logout failed, the status code will be 400 BAD REQUEST.
        """
        # Check if a user session exists
        user_id = request.session.get('user')
        print(f'user_id receive email: {user_id}')
        if user_id is None:
            return Response([], status=status.HTTP_200_OK)
        # If a user session exists, call the list method of the superclass
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        """
        Retrieves the queryset of emails received by the logged-in user.

        Returns:
            - A queryset of Emails objects where the recipient is the logged-in user.
        """
        # Get the user id from the session
        user_id = self.request.session.get('user')
        # Return the emails where the recipient is the user
        return Emails.objects.filter(recipient_id=user_id)