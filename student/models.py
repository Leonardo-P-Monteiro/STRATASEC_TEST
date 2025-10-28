from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,\
            verbose_name="Nome", on_delete=models.CASCADE)
    e_mail = models.EmailField(verbose_name='E-mail', max_length=254,\
                unique=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Telefone')

    class Meta:
        ordering = ['user__username']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_user_student(sender, instance, **kwargs):
        instance.student.save()