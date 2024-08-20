from django.db import models
from course.models import Course
from teacher.models import Teacher

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=20)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)
    coursename = models.ManyToManyField(Course)

    def __str__(self):
        return self.classroom