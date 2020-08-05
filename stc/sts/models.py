from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher(models.Model):
    name = models.CharField(unique=True, max_length=50)
    # email = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(unique=True, max_length=50)
    # email = models.CharField(max_length=50, blank=False, null=False)
    teachers = models.ManyToManyField(Teacher, through='SubjectClass')

    def __str__(self):
        return self.name


class SubjectClass(models.Model):
    # standard = models.IntegerField(default=1, validators=[MaxValueValidator(12), MinValueValidator(1)])
    # subject = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_starred = models.BooleanField(default=False)

    class Meta:
        unique_together = [['teacher', 'student']]

    def __str__(self):
        return "'{0}'-'{1}'".format(self.teacher, self.student)
#
# class Starred(models.Model):
#     is_starred = models.BooleanField(default=False)
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     subject_class = models.OneToOneField(SubjectClass, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "'{0}'-'{1}'-'{2}'-'{3}'".format(self.student.name, self.subject_class.standard, self.subject_class.subject, self.student.name)
