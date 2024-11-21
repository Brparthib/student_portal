from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Lecture, Attendance

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to the appropriate dashboard based on the user's role
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            else:  # Assume student by default
                return redirect('student_dashboard')
        else:
            # Optionally, add a message for invalid login
            return render(request, 'portal/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'portal/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def admin_dashboard(request):
    # Fetch all users, lectures, and attendance records
    users = User.objects.all()
    lectures = Lecture.objects.all()
    attendance_records = Attendance.objects.select_related('lecture', 'student')

    return render(request, 'portal/admin_dashboard.html', {
        'users': users,
        'lectures': lectures,
        'attendance_records': attendance_records
    })

def faculty_dashboard(request):
    # Fetch lectures for the logged-in faculty
    lectures = Lecture.objects.filter(faculty=request.user)

    # Fetch attendance records linked to these lectures
    attendance_records = Attendance.objects.filter(lecture__in=lectures).select_related('lecture', 'student')

    # Fetch all students for marking attendance
    students = User.objects.filter(role='student')

    return render(request, 'portal/faculty_dashboard.html', {
        'lectures': lectures,
        'students': students,
        'attendance_records': attendance_records
    })


def student_dashboard(request):
    attendance_records = Attendance.objects.filter(student=request.user)
    return render(request, 'portal/student_dashboard.html', {'attendance_records': attendance_records})
