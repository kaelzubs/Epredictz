from django.urls import path
from .views import list_home, list_home_yesterday

urlpatterns = [
    path('', list_home, name='list_home'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday')
]
