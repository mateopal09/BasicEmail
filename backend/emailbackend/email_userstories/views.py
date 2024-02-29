#Backend
from .models import Emails, User
from .serializers import EmailSendSerializer, EmailRecieveSerializer, RegisterUserSerializer, LoginUserSerializer

#django
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

#django rest framework
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterUserView(generics.CreateAPIView):
    """
    Register View

    This will register a user with name, email, password and photoprofile

    Methods:
    - Post: Return a status code 201 if it's created
    """
    #Specify the serializer class
    serializer_class = RegisterUserSerializer

    def post(self, request):
        """
        Post

        Parameters:

        - Request: Request with the data sent from post method
        
        Return Serializer with data, 201 status code  
        """
        #Save the data of serializer
        serializer = self.get_serializer(data=request.data)
        #Check if serializer has a data if not return a error
        serializer.is_valid(raise_exception=True)
        #If serializer has data it store that data
        self.perform_create(serializer)
        #Headers will have the data saved
        headers = self.get_success_headers(serializer.data)
        return Response (serializer.data, status=status.HTTP_201_CREATED, headers= headers)
    

class LoginUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Login User View

    This will post an email and password to log in a user

    Methods:
    - Post
    """
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        """
        Post

        Return the user 
        """
        
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.password == password:
            request.session['user'] = user.id
            return Response({"detail": "User logged in successfully", 'user': LoginUserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        user_id = request.session.get('user')
        if user_id is None:
            return Response({"detail": "No user logged in"}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()
        try:
            user = User.objects.get(id=user_id)
            user_data = LoginUserSerializer(user).data
            received_emails = Emails.objects.filter(recipient_id=user_id)
            received_emails_data = EmailRecieveSerializer(received_emails, many=True).data
            return Response({
                'user': user_data,
                'received_emails': received_emails_data,
            })
        except ObjectDoesNotExist:
            return Response({"detail": "User not found in get"}, status=status.HTTP_404_NOT_FOUND)
        



class SendEmailView(generics.CreateAPIView):
    """
    Send Email View

    This class will send an Email

    Methods.
    - Post: Post a email
    """
    serializer_class = EmailSendSerializer

    def create(self, request, *args, **kwargs):
        """
        Post

        Parameters:
        - request: It will have the data to send
        - format=None: Django will determine the format of input data

        This will save an instance of the serializer for the data request it
        Then if serializer has a data it will save it, and with a status code 200
        If not it will return 400 status code
        """
        user_id = request.session.get('user')
        if user_id is None:
            return Response({"detail":"No user logged in. Please log in to send an email."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sender = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist:
            return Response({"detail":"User not found"}, status=status.HTTP_404_NOT_FOUND)

        recipient_email = request.data.get('recipient_email')  # El correo electrónico del destinatario
        if recipient_email is None:
            return Response({"detail":"Recipient email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            recipient = get_user_model().objects.get(email=recipient_email)
        except get_user_model().DoesNotExist:
            return Response({"detail":"Recipient not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['sender'] = sender.id
        data['recipient'] = recipient.id
        serializer = EmailSendSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Envía un correo electrónico
            send_mail(
                subject=serializer.validated_data['subject'],
                message=serializer.validated_data['body'],
                from_email=sender.email,
                recipient_list=[recipient.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecievedEmailView(generics.ListAPIView):
    """
    Email Recieved View

    This class received an email sent

    Methods get
    """
    serializer_class = EmailRecieveSerializer
    def get_queryset(self):
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
    
        user_id = self.request.session.get('user')
        if user_id is None:
            return Response({"detail":"No user logged in. Please log in to view received emails."}, status=status.HTTP_400_BAD_REQUEST)

        return Emails.objects.filter(recipient_id=user_id)