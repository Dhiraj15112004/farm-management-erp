from django.contrib import admin
from .models import Worker, Attendance, LaborTask

admin.site.register(Worker)
admin.site.register(Attendance)
admin.site.register(LaborTask)