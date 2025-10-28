from django.contrib import admin
from .models import Resource

# Register your models here.

@admin.register(Resource)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = 'name', 'description', 'course',
    search_fields = 'name', 'course',
