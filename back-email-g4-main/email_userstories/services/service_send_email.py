#Backend
from ..models import Emails
#django
from django.contrib.auth import get_user_model


def service_send_email(request):
    user_id = request.session.get('user')
    if user_id is None:
        raise Exception("No user logged in")

    #Validate if the user_id has email
    sender = get_user_model().objects.get(id=user_id)
    print(sender)
    if sender is None:
        raise Exception("Sender not logged in")

    #Validate the recipient email from the request
    recipient_id = request.data.get('recipient_email')
    if recipient_id is None:
        raise Exception ("Recipient email is required.")
   
    recipient = get_user_model().objects.get(email=recipient_id)
    if recipient is None:
        raise ("Recipient not found")
    
    #Data to deserialize and save in the data base
    subject = request.data.get('subject')
    body = request.data.get('body')
    email = Emails.objects.create(sender=sender, recipient=recipient, subject=subject, body=body)
    email.save()
    return "Email sent succesfully"