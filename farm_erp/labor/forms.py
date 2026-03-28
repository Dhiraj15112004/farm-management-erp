from django import forms
from .models import Worker, Attendance, LaborTask


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'phone', 'role', 'daily_wage']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['worker', 'date', 'status']


class LaborTaskForm(forms.ModelForm):
    class Meta:
        model = LaborTask
        fields = ['task_name', 'worker', 'date', 'status']