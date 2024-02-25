from django.db import models

class Emails (models.Model):
    """
    Emails

    Parameters:
    - models.model: We heritage Model from models to use the django ORM for creating the table 
                    to use in this Email project

    id: Primary key.
    recipient_email: The email address of the recipient to whom the email is sent.
    sender_email: The email address of the sender who sent the email.
    subject: The subject of the email.
    body: The main text content of the email.
    timestamp: The date and time when the email was sent or received.
    """
    id = models.AutoField(primary_key=True)
    recipient_email = models.CharField(max_length=255)
    sender_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    #name
    #profile_picture.
    
