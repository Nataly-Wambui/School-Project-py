from django.shortcuts import render
from datetime import timedelta, timezone

from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from course.models import Course

from.serializers import MinimalStudentSerializer
from.serializers import MinimalTeacherSerializer
from.serializers import MinimalClassroomSerializer
from.serializers import MinimalClassPeriodSerializer
from.serializers import MinimalCourseSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

## Student
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = MinimalStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class StudentDetailView(APIView):
    def enroll_student(self,student,course_code):
        course=Course.objects.get(id=course_code)
        student.course.add(course)
    def post(self,request,id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action=="enroll":
            course_code=request.data.get("course")
            student_id=request.data.get("Student")
            student=Student.objects.get(id=student_id)
            self.enroll_student(student,course_code)
            return  Response(status.HTTP_201_CREATED)
        
    def get(self, request, id):
        student= Student.objects.get(id=id)
        serializer = MinimalStudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer= MinimalStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def email_student(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.course.add(course)
    
    def post(self, request, id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action ("enroll"):
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)
        return Response(status.HTTP_202_ACCEPTED)


## Teacher
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MinimalTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher= Teacher.objects.get(id=id)
        serializer = MinimalTeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer= MinimalTeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class WeeklyTimetableView(APIView):
    def get(self,request):
        now=timezone.now()
        start_of_week =now -timedelta(days=now.weekday())
        end_of_week =start_of_week + timedelta(days=6)

        class_periods = ClassPeriod.objects.filter(
            start_time_gte = start_of_week,
            end_time_lte = end_of_week
        )
        timetable_data ={
            "start_of_week":start_of_week.isoformat(),
            "end_of_week":end_of_week.isoformat(),
            "class_periods": MinimalClassPeriodSerializer(class_periods, many=True).data
            }
        return Response(timetable_data,status=status.HTTP_200_OK)



## Classroom 
    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = MinimalClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MinimalClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom= Classroom.objects.get(id=id)
        serializer = MinimalClassroomSerializer(classroom)
        return Response(serializer.data)
    
    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer= MinimalClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    



## Classperiod
    
class ClassperiodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MinimalClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod= ClassPeriod.objects.get(id=id)
        serializer = MinimalClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer= MinimalClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




## Course
    
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = MinimalCourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MinimalCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CourseDetailView(APIView):
    def get(self, request, id):
        course= Course.objects.get(id=id)
        serializer = MinimalCourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer= MinimalCourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self,request,id):
        course=Course.objects.get(id=id)
        action=request.data.get("action")
        if action =="assign_teacher":
            teacher_id=request.data.get("teacher")
            teacher=Teacher.objects.get(id=teacher_id)
            course.teacher.add(teacher)
            return Response ({"status":"teacher assigned"} , status=status.HTTP_201_CREATED)
        return Response ({"error":"invalid action"},status=status.HTTP_400_BAD_REQUEST)