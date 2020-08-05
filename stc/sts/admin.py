from django.contrib import admin
from . models import Teacher, Student, SubjectClass
# Register your models here.


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(SubjectClass)