from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from training.models import Training

# Create your models here.

class Course(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    training = models.ForeignKey(Training, verbose_name='Treinamento', \
                on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(verbose_name='Data de Início', blank=True, \
                    null=True)
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', \
                        blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def clean(self):
        print(self.slug)
        if not self.slug:
            new_slug = slugify(self.name)
            print(new_slug)

            self.slug = new_slug

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    #TODO: Fazer o link - Class
    def get_absolute_url(self):
        return reverse('course:detail', args=[self.pk])
    
    def __str__(self):
        return self.name