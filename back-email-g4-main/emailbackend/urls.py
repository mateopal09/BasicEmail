"""
URL configuration for emailbackend project.
"""
#Django 
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Local
from email_userstories.controller.login import LoginUserView
from email_userstories.controller.logout import LogoutView
from email_userstories.controller.register_user import RegisterUserView
from email_userstories.controller.send_email import SendEmailView
from email_userstories.controller.recieved_email import RecievedEmailView


schema_view = get_schema_view(
   openapi.Info(
      title="Email API",
      default_version='v1',
      description="email API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="home-group-4@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/',RegisterUserView.as_view(),name='register'),
    path('api/login/',LoginUserView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/send-email/', SendEmailView.as_view(),name='send_email'),
    path('api/recieve-email/<str:email>/',RecievedEmailView.as_view(), name='received_email'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  ]
