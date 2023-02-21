from django.urls import path
from .views import voteLike, list_calender, list_home, list_home_today, list_home_yesterday, list_home_tomorrow


urlpatterns = [
    path('', list_home, name='list_home'),
    path('today/', list_home_today, name='list_home_today'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday'),
    path('tomorrow/', list_home_tomorrow, name='list_home_tomorrow'),
    path('<int:year>/<str:month>/<int:day>/', list_calender, name='calender'),
    path('vote/<int:pk>', voteLike, name="vote_like")
]
