from django.urls import path
from .views import ShaxsListView

urlpatterns = [
  path('', ShaxsListView.as_view(), name="home")
]
