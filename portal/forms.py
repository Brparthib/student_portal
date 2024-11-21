from django import forms
from .models import User, Lecture, Attendance
        
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['subject', 'faculty', 'time']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'lecture', 'status']
