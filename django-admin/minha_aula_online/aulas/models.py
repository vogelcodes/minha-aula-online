from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    class Meta:
        verbose_name = 'Aluno'

    def __str__(self) -> str:
        return self.first_name



class Lecture_template(models.Model):
    template_name = models.CharField(max_length=255)
    lecture_title = models.CharField(max_length=255)
    lecture_subject = models.CharField(max_length=255)
    lecture_descript = models.TextField()
    class Meta:
        verbose_name = 'Template'

    def __str__(self) -> str:
        return self.template_name


class Lecture(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    date = models.DateTimeField(verbose_name='Data')
    subject = models.CharField(max_length=255, blank=True, verbose_name='Assunto')
    description = models.TextField(blank=True, verbose_name='Descrição')
    template = models.ForeignKey(Lecture_template, blank=True, on_delete=models.SET_NULL, null=True)
    attendees = models.ManyToManyField(Student, blank=True)

    class Meta:
        verbose_name = 'Aula'
    def __str__(self) -> str:
        return self.title
    @property
    def num_of_att(self):
        return self.attendees.all().count()
    num_of_att.fget.short_description = 'Inscritos'

