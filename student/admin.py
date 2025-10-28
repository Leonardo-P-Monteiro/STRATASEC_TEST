from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'user__username', 'e_mail', 'phone',
    search_fields = 'user__username', 'e_mail', 'phone',