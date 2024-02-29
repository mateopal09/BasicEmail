from rest_framework import serializers

from email_userstories.models import Emails, User

class EmailSendSerializer(serializers.ModelSerializer):
    """
    EmailSerializer

    It will render the instances of the model Emails into JSON

    Attributes:
        - Meta.model: Model class that will be serialized.
        - Meta.fields: Fields of the Emails model that are included in the serialized representation.  
    """
    class Meta:
        model = Emails
        fields = ['recipient','sender', 'subject', 'body', 'timestamp']


class EmailRecieveSerializer(serializers.ModelSerializer):
    """
    Email Receive

    This is for receive email

    Attributes:
    - Meta.model = User class
    - Meta.field = The fields to serialize are email, name, password and photo_profile
    """
    class Meta:
        model = Emails
        fields = ['sender_id', 'subject','body','timestamp']


class LoginUserSerializer(serializers.ModelSerializer):
    """
    Login User

    This is for log in a user

    Attributes:
    - Meta.model = User
    - Meta.field = The fields to serialize are email and password    
    """
    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Register User

    This is for Register a User

    Attributes:
    - Meta.model = User
    - Meta.model = The fields to serialize are name, email,password, photo_profile
    """
    class Meta:
        model= User
        fields = ['name', 'email','password', 'photo_profile']

