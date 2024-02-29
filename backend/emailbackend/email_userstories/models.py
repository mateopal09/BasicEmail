#django
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class MyUserManager(BaseUserManager):
    """
    User manager

    Methods:
    - Create_user: It will create the user
    """

    def create_user(self, email, password=None):
        """
        Create user

        Parameter:
        - Email: User email
        - Password: User password

        return User with the email and password
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):
    """
    User

    Attributes:
    - Email: Email
    - name : user name
    - photo_profile: Use photo
    """
    #
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    photo_profile = models.ImageField(blank=True, null=True)

    #Instance of MyUserManager to handle this model
    objects = MyUserManager()

    #Username_field is email not username
    USERNAME_FIELD = 'email'


# class User(models.Model):
#     """
#     Users Profile

#     Name: Charfield with max_length 255
#     email: EmailField
#     password: Charfield with max_length 255
#     photo_profile: ImageField blank and null True
#     """
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     photo_profile = models.ImageField(blank=True, null=True)

class Emails(models.Model):
    """
    Emails

    Parameters:
    - models.model: We heritage Model from models to use the django ORM for creating the table 
                    to use in this Email project

    id: Primary key.
    recipient_id = The recipient id is where I send the email
    sender_id = Who sent the email
    recipient_email: The email address of the recipient to whom the email is sent.
    sender_email: The email address of the sender who sent the email.
    subject: The subject of the email.
    body: The main text content of the email.
    timestamp: The date and time when the email was sent or received.
    name: The name of the user. Null is for the db to be null, and in the form is for being blank=True the space, It means don't require
    profile_picture: It will store an image of the user, and it is not required
    """
    recipient = models.ForeignKey(User, related_name='received_emails', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender_email', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
