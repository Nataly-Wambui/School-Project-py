from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    age = models.PositiveIntegerField()
    gender = models.PositiveSmallIntegerField()
    classes = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
