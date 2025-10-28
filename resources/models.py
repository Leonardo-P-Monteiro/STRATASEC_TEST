from django.db import models
from course.models import Course

# Create your models here.

CHOICES_RESOURCE = [
    ('V', 'VÍDEO'),
    ('P', 'PDF'),
    ('Z', 'ZIP')
]

class Resource(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descrição', max_length=5000,\
                    null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name='Turma', \
                on_delete=models.CASCADE)
    type_resource = models.CharField(choices=CHOICES_RESOURCE, max_length=1)
    previous_acess = models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], \
                        max_length=1)
    draft = models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], \
                        max_length=1)

    class Meta:
        ordering = ['name']
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
    
    def __str__(self):
        return self.name