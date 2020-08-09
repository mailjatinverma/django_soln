import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Teacher, Student, SubjectClass


# Create a GraphQL type for the teacher model
class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


# Create a GraphQL type for the movie model
class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class SubjectClassType(DjangoObjectType):
    class Meta:
        model = SubjectClass


# Create a Query type
class Query(ObjectType):
    teacher = graphene.Field(TeacherType, id=graphene.Int())
    student = graphene.Field(StudentType, id=graphene.Int())
    subject_class = graphene.Field(SubjectClassType, id=graphene.Int())
    teachers = graphene.List(TeacherType)
    students= graphene.List(StudentType)
    subject_classes = graphene.List(SubjectClassType)

    def resolve_teacher(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Teacher.objects.get(pk=id)

        return None

    def resolve_student(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Student.objects.get(pk=id)

        return None

    def resolve_subject_class(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return SubjectClass.objects.get(pk=id)

        return None

    def resolve_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_subject_classs(selfself, info, **kwargs):
        return SubjectClass.objects.all()


# Create Input Object Types
class TeacherInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class StudentInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class SubjectClassInput(graphene.InputObjectType):
    # check for graphene.List or just Field
    teacher = graphene.Field(TeacherInput)
    student = graphene.Field(StudentInput)
    is_starred = graphene.Boolean()


# Create Mutations for Teacher, Student, SubjectClass

class CreateTeacher(graphene.Mutation):
    class Arguments:
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        teacher_instance = Teacher(name=input.name)
        teacher_instance.save()
        return CreateTeacher(ok=ok, teacher=teacher_instance)


class UpdateTeacher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        teacher_instance = Teacher.objects.get(pk=id)
        if teacher_instance:
            ok = True
            teacher_instance.name = input.name
            teacher_instance.save()
            return UpdateTeacher(ok=ok, teacher=teacher_instance)
        return UpdateTeacher(ok=ok, teacher=None)


class CreateStudent(graphene.Mutation):
    class Arguments:
        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        student_instance = Student(name=input.name)
        student_instance.save()
        return CreateStudent(ok=ok, student=student_instance)


class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        student_instance = Student.objects.get(pk=id)
        if student_instance:
            ok = True
            student_instance.name = input.name
            student_instance.save()
            return UpdateStudent(ok=ok, student=student_instance)
        return UpdateStudent(ok=ok, student=None)


class CreateSubjectClass(graphene.Mutation):
    class Arguments:
        input = SubjectClassInput(required=True)

    ok = graphene.Boolean()
    subject_class = graphene.Field(SubjectClassType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        teacher_input = input.teacher
        teacher = Teacher.objects.get(pk=teacher_input.id)
        if teacher is None:
            return CreateSubjectClass(ok=False, subject_class=None)
        student_input = input.student
        student = Student.objects.get(pk=student_input.id)
        if student is None:
            return CreateSubjectClass(ok=False, subject_class=None)
        is_starred = input.is_starred
        subject_class_instance = SubjectClass(teacher=teacher, student=student, is_starred=is_starred)
        subject_class_instance.save()
        return CreateSubjectClass(ok=ok, subject_class=subject_class_instance)


class UpdateSubjectClass(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = SubjectClassInput(required=True)

    ok = graphene.Boolean()
    subject_class = graphene.Field(SubjectClassType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        subject_class_instance = SubjectClass.objects.get(pk=id)
        if subject_class_instance:
            ok = True
            teacher_input = input.teacher
            teacher = Teacher.objects.get(pk=teacher_input.id)
            if teacher is None:
                return UpdateSubjectClass(ok=False, subject_class=None)
            student_input = input.student
            student = Student.objects.get(pk=student_input.id)
            if student is None:
                return UpdateSubjectClass(ok=False, subject_class=None)
            is_starred = input.is_starred
            subject_class_instance.teacher = teacher
            subject_class_instance.student = student
            subject_class_instance.is_starred = is_starred
            subject_class_instance.save()
            return UpdateSubjectClass(ok=ok, subject_class=subject_class_instance)
        return UpdateSubjectClass(ok=ok, subject_class=None)


class Mutation(graphene.ObjectType):
    create_teacher = CreateTeacher.Field()
    update_teacher = UpdateTeacher.Field()

    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()

    create_subject_class = CreateSubjectClass.Field()
    update_subject_class = UpdateSubjectClass.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)











