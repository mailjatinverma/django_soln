from django.test import TestCase
from . models import Teacher, Student, SubjectClass
from django.urls import reverse # new
# Create your tests here.


class STSTest(TestCase):

    def setUp(self):
        teacher_1 = Teacher.objects.create(name="Teacher1")
        student_1 = Student.objects.create(name="Student1")
        subjectclass_1 = SubjectClass(teacher=teacher_1, student=student_1, is_starred=True)

    def test_string_representation(self):
        teacher = Teacher(name="TeacherNo1")
        self.assertEqual(str(teacher), teacher.name)

        student = Student(name="StudentNo1")
        self.assertEqual(str(student), student.name)

        subject_class = SubjectClass(teacher=teacher, student=student, is_starred=True)
        self.assertEqual(str(subject_class), "'{0}'-'{1}'".format(teacher.name, student.name))

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/teacher/')
        self.assertEqual(resp.status_code, 200)

        response = self.client.get('/student/')
        self.assertEqual(response.status_code, 200)

        response_sc = self.client.get('/subjectclass/')
        self.assertEqual(response_sc.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('teacher_list'))
        self.assertEqual(resp.status_code, 200)

        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)

        response_sc = self.client.get(reverse('subjectclass_list'))
        self.assertEqual(response_sc.status_code, 200)

    def test_teacher_list_view(self):
        resp = self.client.get(reverse('teacher_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Teacher1")
        self.assertTemplateUsed(resp, 'teacher_list.html')

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student1")
        self.assertTemplateUsed(response, 'student_list.html')

    def test_subject_class_list_view(self):
        response = self.client.get(reverse('subjectclass_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "Student1")
        self.assertTemplateUsed(response, 'subjectclass_list.html')

    def test_teacher_detail_view(self):
        response = self.client.get('/teacher/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/teacher/100000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, "Teacher1")
        self.assertTemplateUsed(response, 'teacher_detail.html')

    def test_student_detail_view(self):
        response = self.client.get('/student/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/student/100000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, "Student1")
        self.assertTemplateUsed(response, "student_detail.html")

    def test_subject_class_detail_view(self):
        # ??
        response = self.client.get('/subjectclass/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/subjectclass/100000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, "Student1")
        self.assertTemplateUsed(response, "subjectclass_detail.html")
