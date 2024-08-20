from django.db import models
from teacher.models import Teacher


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    course_code = models.CharField(max_length=20)
    topics = models.CharField(max_length=20)
    teacher_in_charge = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    students_enrolled = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    teachers = models.ManyToManyField(Teacher, related_name='courses', blank=True)
    assessment_method = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title} {self.course_code}"
