from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentID', 'FirstName', 'LastName', 'Email', 'DateOfBirth', 'Course', 'EnrollmentDate')

admin.site.register(Student, StudentAdmin)