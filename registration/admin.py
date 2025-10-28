from django.contrib import admin
from .models import Registration

# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = 'student', 'course',
    search_fields = 'student__name', 'course__name',