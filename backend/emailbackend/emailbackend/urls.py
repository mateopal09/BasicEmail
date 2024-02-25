"""
URL configuration for emailbackend project.
"""
#Django 
from django.contrib import admin
from django.urls import path

#Local
from email_userstories.views import SendEmailView, RecievedEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/send-email/', SendEmailView.as_view(),name='send_email'),
    path('api/recieve-email/<str:sender_email>/',RecievedEmailView.as_view(), name='received_email'),
]
