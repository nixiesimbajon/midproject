from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def save(request):
    if request.method == 'POST':
        StudentID = request.POST['StudentID']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Email = request.POST['Email']
        DateOfBirth = request.POST['DateOfBirth']
        Course = request.POST['Course']
        EnrollmentDate = request.POST['EnrollmentDate']

        student = Student(StudentID=StudentID, FirstName=FirstName, LastName=LastName, Email=Email, DateOfBirth=DateOfBirth, Course=Course, EnrollmentDate=EnrollmentDate)
        student.save()

        return redirect('stud_list')
    else:
        return redirect('/')  # Redirect to the index page if the request method is GET

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})

def update(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.StudentID = request.POST['StudentID']
        student.FirstName = request.POST['FirstName']
        student.LastName = request.POST['LastName']
        student.Email = request.POST['Email']
        student.DateOfBirth = request.POST['DateOfBirth']
        student.Course = request.POST['Course']
        student.EnrollmentDate = request.POST['EnrollmentDate']
        student.save()

        return redirect('stud_list')
    else:
        return redirect('/') 

def delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('stud_list')
    return render(request, 'confirm_delete.html', {'student': student})

def stud_list(request):
    students = Student.objects.all()
    return render(request, 'stud_list.html', {'students': students})