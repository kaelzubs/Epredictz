from django.urls import path
from .views import list_home

urlpatterns = [
    path('', list_home.as_view(), name='list_home'),
]
