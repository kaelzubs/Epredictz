from django.urls import path
from .views import CalendarView, vote_up, vote_down, list_home, list_home_today, list_home_yesterday, list_home_tomorrow


urlpatterns = [
    path('', list_home, name="list_home"),
    path('likes-prediction/<int:pk>/', vote_up, name='like'),
    path('dislikes-prediction/<int:pk>/', vote_down, name='dislike'),
    path('today/', list_home_today, name='list_home_today'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday'),
    path('tomorrow/', list_home_tomorrow, name='list_home_tomorrow'),
    path(’calendar/’, CalendarView.as_view(), name=’calendar’)
]
