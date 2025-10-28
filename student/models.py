from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    e_mail = models.EmailField(verbose_name='E-mail', max_length=254,\
                unique=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Telefone')

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def __str__(self):
        return self.name