from django.contrib import admin
from .models import Registration

# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = 'student', 'course',
    search_fields = 'student', 'course', #TODO: Resolver o problema de não conseguir buscar por esses campos no admin do Django. Veja se é realmente necessário pra lógica do programa.