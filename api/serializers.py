from rest_framework import serializers

from student.models import Student
from classperiod.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["id","title","course_code","duration"]

class CourseSerializer(serializers.ModelSerializer):
    teachers=TeacherSerializer(many=True)
    class Meta:
        model = Course
        fields = "__all__"



class MinimalStudentSerializer(serializers.ModelSerializer):
     full_name=serializers.SerializerMethodField()
     def get_full_name(self,object):
        return f"{object.firstName} {object.lastName}"
     class Meta:
        model=Student
        fields=["id","full_name","email"]

class StudentSerializer(serializers.ModelSerializer):
    course_details=CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = "__all__"




class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields=["id","start_time","end_time"]  

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"


class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Teacher
        fields=["id","full_name","email","course","specialization"]

class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=["id","name","number_of_groups"]


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"



