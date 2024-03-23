from ..serializers import  RegisterUserSerializer
#rest-framework
from rest_framework import status, generics
from rest_framework.response import Response


class RegisterUserView(generics.CreateAPIView):
    """
    Register View

    This view handles the registration of a new user. It accepts a POST request containing user data,
    validates this data using the RegisterUserSerializer, and then saves the new user to the database.

    Attributes
        - serializer_class: The serializer class for this view will use to validate and deserialize input, and to serialize output.

    Methods
        - Post(request): Handles a POST request. It creates a new serializer with the data from the request, 
          validates the data, and then saves the validated data as a new user in the database.
    """
    #Specify the serializer class
    serializer_class = RegisterUserSerializer

    def post(self, request):
        """
        Register user.

        Parameters 
        - request the request.data should contain the user data to be validated and saved
        
        Return 
            - A Response object  with the serialized data of the newly created user and a status code indicating the success of the operation.
              If the operation was succesful, the status code will be 201 CREATED.
        """
        #Save the data of serializer
        serializer = self.get_serializer(data=request.data)
        #Validate the data. if the data is invalid, a 400 BAD REQUEST respoonse will be raised
        serializer.is_valid(raise_exception=True)
        #If serializer has data it store that data in the database
        self.perform_create(serializer)
        #Headers will have the data saved
        headers = self.get_success_headers(serializer.data)
        # Return a 201 CREATED response with the serialized data of the new user
        return Response (serializer.data, status=status.HTTP_201_CREATED, headers= headers)