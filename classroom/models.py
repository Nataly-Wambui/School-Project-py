from django.db import models
from teacher.models import Teacher
from course.models import Course
from student.models import Student

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField()
    topics = models.EmailField()
    number_of_groups = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=20)
    courses = models.PositiveSmallIntegerField()
    schedule = models.CharField(max_length=20)
    artwork = models.CharField(max_length=20)
    class_reperesentative = models.CharField(max_length=20)
    room_number = models.PositiveSmallIntegerField()
    teacher = models.ManyToManyField(Teacher)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classroom', blank=True)
    def __str__(self):
        return f"{self.name} {self.room_number}"