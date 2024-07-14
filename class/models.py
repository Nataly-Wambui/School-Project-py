from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField()
    topics = models.EmailField()
    number_of_groups = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=20)
    courses = models.PositiveSmallIntegerField(max_length=20)
    schedule = models.CharField(max_length=20)
    artwork = models.CharField(max_length=20)
    class_reperesentative = models.CharField(max_length=20)
    room_number = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.name} {self.room_number}"