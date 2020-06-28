from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<str:id>/", views.UserView.as_view()),
    path("userss/", views.UserAPIView.as_view()),
]