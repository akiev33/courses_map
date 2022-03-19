from django.urls import path
from .views import FavoriteCreateAPIView, FavoriteAPIView, FavoriteDeleteAPIView

urlpatterns = [
    path('create/', FavoriteCreateAPIView.as_view()),
    path('list/', FavoriteAPIView.as_view()),
    path('list/<int:id>/', FavoriteDeleteAPIView.as_view()),

]