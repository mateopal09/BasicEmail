#django
from django.contrib.auth import get_user_model


#rest-framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutView(APIView):
    def post(self, request):
        """
        Handles a POST request to log out the user.

        Parameters:
            - request: The request that triggered this method.

        Returns:
            - A Response object with a message indicating the success or failure of the logout process. If the logout was successful, the status code will be 200 OK. If the logout failed, the status code will be 400 BAD REQUEST.
        """
        # Validate if the session of the user exist
        user_id = request.session.get('user')
        print(f'user id logout {user_id}')
        if user_id is None:
            return Response({"detail": "No user logged in"}, status=status.HTTP_400_BAD_REQUEST)

        # This is the model to use
        User = get_user_model()
        # Check if the user exists in the database
        if User.objects.filter(id=user_id).exists():
            # Delete the user session
            del request.session['user']
            return Response({"detail": "User logged out successfully"}, status=status.HTTP_200_OK)
        # If user doesn't exist it response a 404 NOT FOUND
        else:
            return Response({"detail": "User not found in post"}, status=status.HTTP_404_NOT_FOUND)