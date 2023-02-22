from django.urls import path, re_path
from .views import list_calender, list_home, list_detail, list_home_today, list_home_yesterday, list_home_tomorrow


urlpatterns = [
    path('', list_home, name="list_home"),
    path('vote/<int:pk>/', list_detail, name="list_detail"),
    path('today/', list_home_today, name='list_home_today'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday'),
    path('tomorrow/', list_home_tomorrow, name='list_home_tomorrow'),
    path('<int:year>/<str:month>/<int:day>/', list_calender, name='calender')
]
