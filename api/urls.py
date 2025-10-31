from django.contrib import admin
from django.urls import path
from .views import CourseListCreateView, RegistrationListCreateView, \
      ResourceListCreateView, ResourceDetailView, StudentListCreateView

app_name = 'api'

urlpatterns = [
    path('course/', CourseListCreateView.as_view()),
    path('registration/', RegistrationListCreateView.as_view()),
    path('resource/', ResourceListCreateView.as_view()),
    path('resource/<int:pk>/', ResourceDetailView.as_view()),
    path('student/', StudentListCreateView.as_view()),
]