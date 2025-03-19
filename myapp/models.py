from django.db import models

# Create your models here.

class Student(models.Model):
    StudentID = models.IntegerField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    DateOfBirth = models.DateField()
    Course = models.CharField(max_length=100)
    EnrollmentDate = models.DateField()

    