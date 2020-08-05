from django.test import TestCase
from . models import Teacher, Student, SubjectClass
from django.urls import reverse # new
# Create your tests here.


class TeacherListViewTest(TestCase):

    def setup(self):
        teacher_1 = Teacher.objects.create(name="Teacher1")
        student_1 = Student.objects.craete(name="Student1")
        subject_class_1 = SubjectClass(teacher=teacher_1, student=student_1, is_starred=True)

    def test_string_representation(self):
        teacher = Teacher(name="TeacherNo1")
        self.assertEqual(str(teacher), teacher.name)

        student = Student(name="StudentNo1")
        self.assertEqual(str(student), student.name)


    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/teacher/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('teacher_list'))
        self.assertEqual(resp.status_code, 200)

    def test_teacher_list_view(self):
        resp = self.client.get(reverse('teacher_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Teacher1')
        self.assertTemplateUsed(resp, 'teacher_list.html')

    def test_teacher_detail_view(self):
        """???"""
        response = self.client.get('/teacher/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/teacher/100000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, 'Teacher1')
        self.assertTemplateUsed(response, 'teacher_detail.html')