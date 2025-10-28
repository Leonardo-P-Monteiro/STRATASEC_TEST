from django.db import models
from course.models import Course
from student.models import Student

# Create your models here.

class Registration(models.Model):
    course = models.ForeignKey(Course, verbose_name='Turma', \
                on_delete=models.PROTECT, related_name='course_registrations')
    course_search = course.name
    student = models.ForeignKey(Student, verbose_name='Aluno', \
                on_delete=models.PROTECT, related_name='student_registrations')
    
    class Meta:
        ordering = ['student']
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'

    def __str__(self):
        return f'{self.student} - {self.course}'