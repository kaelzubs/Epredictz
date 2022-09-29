from django.urls import path
from .views import list_home




urlpatterns = [

    path('', list_home, name='list_home'),

]