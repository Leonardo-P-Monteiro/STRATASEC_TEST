from django.contrib import admin
from .models import Training

# Register your models here.

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    search_fields = 'name', 'description',