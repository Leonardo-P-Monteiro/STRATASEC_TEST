from django.contrib import admin
from django.urls import path
from .views import CourseDetailView, CourseTemplateView

app_name = 'course'

urlpatterns = [
    path('<int:pk>/detail/', CourseDetailView.as_view(), name='detail'),
    path('video/', CourseTemplateView.as_view(), name='video'), 
]