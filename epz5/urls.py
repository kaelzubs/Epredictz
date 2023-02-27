from django.urls import path
from . views import list_faqs

urlpatterns = [
    path('questions', list_faqs, name='list_faqs'),
]
