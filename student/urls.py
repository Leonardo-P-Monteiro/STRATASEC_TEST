from django.contrib import admin
from django.urls import path
from .views import StudentLoginView, StudentLogoutView, StudentList

app_name = 'student'

urlpatterns = [
    path('', StudentLoginView.as_view(), name='login'),
    path('logout/', StudentLogoutView.as_view(), name='logout'),
    path('home/', StudentList.as_view(), name='home'),
]