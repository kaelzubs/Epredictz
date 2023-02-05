from django.urls import path
from .views import list_home, list_home_prev, list_home_next, list_home_today

urlpatterns = [
    path('', list_home, name='list_home'),
    path('yesterday/', list_home_prev, name='list_home_prev'),
    path('today/', list_home_today, name='list_home_today'),
    path('tomorrow/', list_home_next, name='list_home_next')
]
