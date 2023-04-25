from django.urls import path
from .views import invest_view

urlpatterns = [
    path('odd/', invest_view, name='invest')
]