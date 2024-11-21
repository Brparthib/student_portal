from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

class Lecture(models.Model):
    subject = models.CharField(max_length=100)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'faculty'})
    time = models.DateTimeField()

    def __str__(self):
        return self.subject

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
