from django.urls import path
from . import views

urlpatterns = [
    path('main', views.first_api),
]