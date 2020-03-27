from django.contrib import admin
from django.urls import path
from .views import ProfessorListView,CourseListView, ProfessorDetailView, CourseDetailView
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('profs/', ProfessorListView.as_view(), name='Professors-home'),
    path('profs/<int:pk>', ProfessorDetailView.as_view(), name='prof-detail'),
    path('profs/<int:pk>/add_review', views.add_review, name='add-review'),
    path('courses/', CourseListView.as_view(), name='courses-home'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
]
