from django.urls import path
from . views import list_contact, contact_success

urlpatterns = [
    path('us', list_contact, name='list_contact'),
    path('contact_success', contact_success, name='contact_success'),
]