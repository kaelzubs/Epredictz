from django.urls import path
from .views import ArticleDayArchiveView

urlpatterns = [
    path('', ArticleDayArchiveView.as_view(), name='list_home'),
]
