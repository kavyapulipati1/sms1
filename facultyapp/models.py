# models.py
from django.db import models
from django.contrib.auth.models import User

from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICES=[
        ('AOOP','ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD','PYTHON FULLSTACK DEVELOPMENT'),
        ('CTOOD','COMPUTATIONAL THINKING OBJECT ORIENTED PROGRAMMING')
    ]
    SECTION_CHOICES=[
        ('S11','Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
        ('S14', 'Section S14'),
        ('S15', 'Section S15'),
    ]
    student=models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number}-{self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULLSTACK DEVELOPMENT'),
        ('CTOOD', 'COMPUTATIONAL THINKING OBJECT ORIENTED PROGRAMMING')
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks=models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course}"