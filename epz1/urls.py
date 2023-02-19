from django.urls import path
from .views import query_by_month, list_home, list_home_today, list_home_yesterday, list_home_tomorrow


urlpatterns = [
    path('', list_home, name='list_home'),
    path('pick_date/', query_by_month, name='pick_date'),
    path('today/', list_home_today, name='list_home_today'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday'),
    path('tomorrow/', list_home_tomorrow, name='list_home_tomorrow')
]
