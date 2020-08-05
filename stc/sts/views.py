from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Teacher, Student, SubjectClass
# Create your views here.


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher_new.html'
    fields = ('name',)
    success_url = reverse_lazy('teacher_list')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher_update.html'
    fields = ('name',)


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_delete.html'
    success_url = reverse_lazy('teacher_list')


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_new.html"
    fields = ('name',)
    success_url = reverse_lazy('student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_update.html'
    fields = ('name',)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')


class SubjectClassCreateView(CreateView):
    model = SubjectClass
    template_name = "subjectclass_new.html"
    fields = ('teacher', 'student', 'is_starred',)
    success_url = reverse_lazy('subjectclass_list')


class SubjectClassDetailView(DetailView):
    model = SubjectClass
    template_name = 'subjectclass_detail.html'


class SubjectClassUpdateView(UpdateView):
    model = Student
    template_name = 'subjectclass_update.html'
    fields = ('teacher', 'student', 'is_starred',)


class SubjectClassDeleteView(DeleteView):
    model = Student
    template_name = 'subjectclass_delete.html'
    success_url = reverse_lazy('subjectclass_list')


class SubjectClassListView(ListView):
    model = SubjectClass
    template_name = 'subjectclass_list.html'