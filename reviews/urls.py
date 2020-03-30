from django.contrib import admin
from django.urls import path
from .views import (ProfessorListView,
                    CourseListView,
                    ProfessorDetailView,
                    CourseDetailView,
                    ReviewCreateView,
                    ReviewUpdateView,
                    CourseReviewCreateView,
                    ReviewDeleteView,
                    CourseReviewDeleteView,
                    CourseReviewUpdateView,
                    )
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('profs/', ProfessorListView.as_view(), name='Professors-home'),
    path('profs/<int:pk>/', ProfessorDetailView.as_view(), name='prof-detail'),
    path('profs/<int:pk>/add_review/', ReviewCreateView.as_view(), name='add-review'),
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='update-review'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete-review'),
    path('report/', views.report_review, name='report'),
    path('courses/', CourseListView.as_view(), name='courses-home'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/add_review/', CourseReviewCreateView.as_view(), name='add-course-review'),
    path('c_edit/<int:pk>/', CourseReviewUpdateView.as_view(), name='update-course-review'),
    path('c_delete/<int:pk>/', CourseReviewDeleteView.as_view(), name='delete-course-review'),
    path('c_report/', views.report_course_review, name='c-report')
]
