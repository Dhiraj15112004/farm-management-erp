from django import forms
from .models import Equipment, UsageLog, Maintenance


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type', 'number']


class UsageLogForm(forms.ModelForm):
    class Meta:
        model = UsageLog
        fields = ['equipment', 'date', 'hours', 'fuel_used']


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['equipment', 'date', 'description']