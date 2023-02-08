from django.urls import path
from .views import ArticleDayArchiveView

urlpatterns = [
    #path('', list_home, name='list_home'),
    path('<int:year>/<str:month>/<int:day>/', ArticleDayArchiveView.as_view(), name='archive_day'),
]
