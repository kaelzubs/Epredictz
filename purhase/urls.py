from django.urls import path
from .views import purchase_view

urlpatterns = [
    path('gadgets/', purchase_view, name='purchase')
]
