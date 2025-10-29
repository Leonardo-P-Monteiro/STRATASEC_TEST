from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import Course

# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    template_name = 'details.html'

class CourseTemplateView(TemplateView):
    template_name = 'video.html'