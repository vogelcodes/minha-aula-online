from django.contrib import admin
from .models import Lecture, Lecture_template, Student

# Register your models here.


admin.site.register(Lecture_template)
admin.site.register(Student)

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    filter_horizontal=['attendees']
    list_display = ['title','date','subject', 'num_of_att']
