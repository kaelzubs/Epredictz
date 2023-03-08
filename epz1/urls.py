from django.urls import path
from .views import vote_up, vote_down, list_home, list_home_today, list_home_yesterday, list_home_tomorrow, list_all_prediction


urlpatterns = [
    path('', list_home, name="list_home"),
    path('likes-football-prediction/<int:pk>/', vote_up, name='like'),
    path('dislikes-football-prediction/<int:pk>/', vote_down, name='dislike'),
    path('today-fooball-prediction/', list_home_today, name='list_home_today'),
    path('yesterday-fooball-prediction/', list_home_yesterday, name='list_home_yesterday'),
    path('tomorrow-fooball-prediction/', list_home_tomorrow, name='list_home_tomorrow'),
    path('all-football-prediction-list/', list_all_prediction, name='list_all')
]
