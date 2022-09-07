from django.urls import path
from . views import list_disclaim

urlpatterns = [
    path('condition/', list_disclaim, name='list_disclaim'),
]