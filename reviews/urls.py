from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('profs/', views.prof_home, name='Professors-home'),
]
