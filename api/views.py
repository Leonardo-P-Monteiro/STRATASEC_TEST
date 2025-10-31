from django.shortcuts import render
from course.models import Course
from registration.models import Registration
from resources.models import Resource
from student.models import Student
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import CourseSerializer, RegistrationSerializer, \
     ResourceSerializer, StudentSerializer
from rest_framework.exceptions import PermissionDenied

# COURSE APIVIEWS
class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer

    def get_queryset(self):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem listar todos os cursos.")

        qs = Course.objects.all()

        return qs

    def perform_create(self, serializer):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem criar cursos.")
        
        serializer.save()
    

# REGISTRATION APIVIEWS
class RegistrationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem registrar usuários em cursos.")
        
        serializer.save()

    def get_queryset(self):

        qs = Registration.objects.all() if self.request.user.is_superuser else Registration.objects.filter(student__user = self.request.user)

        return qs

# RESOURCES APIVIEWS
class ResourceListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

    def perform_create(self, serializer):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem registrar novos recursos de cursos.")
        
        serializer.save()

class ResourceDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

# STUDENT APIVIEW
class StudentListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def perform_create(self, serializer):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem listar.")
        
        serializer.save()
    
    def get_queryset(self):

        if not self.request.user.is_superuser:

            raise PermissionDenied(detail="Apenas superusuários podem listar todos os cursos.")

        qs = Course.objects.all()

        return qs