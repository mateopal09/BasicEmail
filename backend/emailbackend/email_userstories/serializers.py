from rest_framework import serializers

from email_userstories.models import Emails

class EmailSerializer(serializers.ModelSerializer):
    """
    EmailSerializer

    It will render the instances of the model Emails into JSON

    Attributes:
        - Meta.model: Model class that will be serialized.
        - Meta.fields: Fields of the Emails model that are included in the serialized representation.  
    """
    class Meta:
        model = Emails
        fields = ['recipient_email', 'subject', 'body', 'timestamp']


class EmailRecieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = ['sender_email', 'subject', 'timestamp']