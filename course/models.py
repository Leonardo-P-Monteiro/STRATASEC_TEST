from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from training.models import Training

# Create your models here.

class Course(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    trainig = models.ForeignKey(Training, verbose_name='Treinamento', \
                on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(verbose_name='Data de Início', blank=True, \
                    null=True)
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', \
                        blank=True, null=True)
    slug = models.SlugField(unique=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    #TODO: Fazer o link - Class
    def get_absolute_url(self):
        return reverse('COLOCAR NOME DA URL', args=[self.slug])
    
    def __str__(self):
        return self.name