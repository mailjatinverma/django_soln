from django.urls import path

from .views import (TeacherCreateView,
                    TeacherDeleteView,
                    TeacherDetailView,
                    TeacherListView,
                    TeacherUpdateView,
                    StudentCreateView,
                    StudentDeleteView,
                    StudentDetailView,
                    StudentListView,
                    StudentUpdateView,
                    SubjectClassCreateView,
                    SubjectClassDetailView,
                    SubjectClassDeleteView,
                    SubjectClassUpdateView,
                    SubjectClassListView,
                    )

urlpatterns = [
    path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('teacher/new', TeacherCreateView.as_view(), name='teacher_new'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),

    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('student/new', StudentCreateView.as_view(), name='student_new'),
    path('student/', StudentListView.as_view(), name='student_list'),

    path('subjectclass/new', SubjectClassCreateView.as_view(), name='subjectclass_new'),
    path('subjectclass/<int:pk>/', SubjectClassDetailView.as_view(), name='subjectclass_detail'),
    path('subjectclass/<int:pk>/delete/', SubjectClassDeleteView.as_view(), name='subjectclass_delete'),
    path('subjectclass/<int:pk>/edit/', SubjectClassUpdateView.as_view(), name='subjectclass_edit'),
    path('subjectclass/', SubjectClassListView.as_view(), name='subjectclass_list'),
]