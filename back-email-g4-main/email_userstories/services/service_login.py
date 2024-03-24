#Backend
from ..models import Emails
from django.contrib.auth.hashers import check_password
#django
from django.contrib.auth import get_user_model
from ..serializers import LoginUserSerializer, EmailRecieveSerializer
from django.core.exceptions import ObjectDoesNotExist

def service_login_post(request):
    """
    service_login_post
    """

    email = request.data.get('email')
    password = request.data.get('password')
    User = get_user_model()

    #Validate if the email exist or no.
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
    #If the user exist and password of the user.password is equal so it will access to that account
    if user is not None and check_password(password, user.password):
        #The session will be the user in this case with his email and its ID
        request.session['user'] = user.id
        print(f'Session_login: {user.id}')
        return LoginUserSerializer(user).data
    return None


def service_login_get(user_id):

    #This is the model to use
    User = get_user_model()
    #Search the user in the database
    try:
        user = User.objects.get(id=user_id)
        user_data = LoginUserSerializer(user).data
        received_emails = Emails.objects.filter(recipient_id=user_id)
        received_emails_data = EmailRecieveSerializer(received_emails, many=True).data
        return {
            'user': user_data,
            'received_emails': received_emails_data,
        }
    #If user doesn't exist it response a 404 NOT FOUND
    except ObjectDoesNotExist:
        return  None

        