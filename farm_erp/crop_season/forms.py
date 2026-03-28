from django import forms
from .models import Season, FieldCropPlan


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'start_date', 'end_date', 'status']


class FieldCropPlanForm(forms.ModelForm):
    class Meta:
        model = FieldCropPlan
        fields = [
            'season',
            'field',
            'crop',
            'sowing_date',
            'expected_harvest_date',
            'expected_yield',
            'expected_budget',
        ]