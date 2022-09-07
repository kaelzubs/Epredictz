from django.urls import path
from . views import list_about

urlpatterns = [
    path('us/', list_about, name='list_about'),
]