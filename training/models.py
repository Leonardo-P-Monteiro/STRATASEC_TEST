from django.db import models

# Create your models here.

class Training(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descrição', \
                    max_length=5000, null=True, blank=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'

    def __str__(self):
        return self.name