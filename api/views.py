from django.shortcuts import render

from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from course.models import Course


from.serializers import StudentSerializer
from.serializers import TeacherSerializer
from.serializers import ClassroomSerializer
from.serializers import ClassPeriodSerializer
from.serializers import CourseSerializer
from rest_framework.response import Response

# Create your views here.


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
class ClassperiodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)