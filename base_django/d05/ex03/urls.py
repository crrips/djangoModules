from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex03, name='ex03'),
]