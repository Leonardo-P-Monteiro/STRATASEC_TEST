from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import Course
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required(login_url='student:login'), name='dispatch')
class CourseDetailView(DetailView):
    model = Course
    template_name = 'details.html'

@method_decorator(login_required(login_url='student:login'), name='dispatch')
class CourseTemplateView(TemplateView):
    template_name = 'video.html'