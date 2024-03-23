#Backend
from ..models import Emails
from ..serializers import LoginUserSerializer, EmailRecieveSerializer
from ..services.service_login import service_login_post, service_login_get

#django
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


#rest-framework
from rest_framework import status, generics
from rest_framework.response import Response


class LoginUserView(generics.GenericAPIView):
    """
    LoginUserView

    This view handles the login process for a user. It accepts a POST request containing the user's email and password,
    validates these credentials, and then logs in the user by storing their user ID in the session.

    Attributes
        - serializer_class: The serializer class that this view will use to validate and deserialize input, 
          and to serialize output.

    Methods
        - post(request, *args, **kwargs): Handles a POST request. It retrieves the email and password from the request data,
          attempts to retrieve a user with the given email, checks if the password is correct, and then logs in the user by
          storing their user ID in the session.
        - get(request): Handles a GET request. It retrieves the user ID from the session, attempts to retrieve a user with
          the given user ID, and then returns a response with the serialized data of the user and their received emails.
    """
    #The serialize class will be LoginUserSerializer 
    serializer_class = LoginUserSerializer

    def post(self, request):
        """
        Handles Login

        Parameters
            - request The request that triggered this method. The request.data should contain the user's email and password.

        Returns
            - A Response object with a message indicating the success or failure of the login process, and the serialized data
              of the user if the login was successful. If the login was successful, the status code will be 200 OK. If the login
              failed, the status code will be 404 NOT FOUND.
        """
        data = service_login_post(request)
        if data:
       
            #It will response a message with the data serialized and a status code
            return Response({"detail": "User logged in successfully", 'user': data}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
            """
            Handles a GET request.

            Parameters
                - request: The request that triggered this method.

            Returns
                - A Response object with the serialized data of the user and their received emails if a user is logged in. If no user
                is logged in, the response will contain a message indicating this and the status code will be 400 BAD REQUEST. If the
                user does not exist, the response will contain a message indicating this and the status code will be 404 NOT FOUND.
            """
            
            #Validate if the session of the user exist
            user_id = request.session.get('user')
            print(f"user id get of login: {user_id}")
            if user_id is None:
                return Response({"detail": "No user logged in"}, status=status.HTTP_400_BAD_REQUEST)
            
            user = service_login_get(user_id)
            #This is the model to use
            if user is not None:
                return Response(user, status=status.HTTP_200_OK)
            #If user doesn't exist it response a 404 NOT FOUND
            else:
                return Response({"detail": "User not found in get"}, status=status.HTTP_404_NOT_FOUND)