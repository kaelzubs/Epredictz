from django.urls import path
from .views import list_home


urlpatterns = [

    path('yesterday/', list_home_prev, name='list_home_prev'),
    path('today/', list_home, name='list_home'),
    path('tomorrow/', list_home_next, name='list_home_next')
]
