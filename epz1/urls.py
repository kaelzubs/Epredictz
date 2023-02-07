from django.urls import path
from .views import ArticleDayArchiveView

urlpatterns = [
    path('<int:year>/<str:month>/<int:day>/', ArticleDayArchiveView.as_view(), name='list_home'),
]
