from django.urls import path
from .views import email_list_signup, sub_success


urlpatterns = [
    path('page', email_list_signup, name='email_list'),
    path('sub-successful', sub_success, name='sub_success')
]
