from django.contrib import admin
from .models import User, Lecture, Attendance

admin.site.register(User)
admin.site.register(Lecture)
admin.site.register(Attendance)
