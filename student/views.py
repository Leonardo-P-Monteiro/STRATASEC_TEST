from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Student
from course.models import Course
from registration.models import Registration
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class StudentLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('student:home')

@method_decorator(login_required(login_url='student:login'), name='dispatch')
class StudentLogoutView(LogoutView):
    next_page = reverse_lazy('student:login')

@method_decorator(login_required(login_url='student:login'), name='dispatch')
class StudentList(ListView):
    """
    Esta view vai exibir a lista de cursos/treinamentos e turmas nas quais
    o estudante está matriculado.
    """
    model = Registration
    template_name = 'home.html'
    login_url = reverse_lazy('student:login')

    def get_queryset(self):
        qs = Registration.objects.filter(student__user=self.request.user)
        course = self.request.GET.get('course')

        if self.request.user.is_superuser:
            qs = Registration.objects.all()

        if course:
            qs = qs.filter(course__training__name__icontains=course)

        return qs
