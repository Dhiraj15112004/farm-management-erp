from django import forms
from .models import FarmProfile, Field, Crop, Equipment


class FarmProfileForm(forms.ModelForm):
    class Meta:
        model = FarmProfile
        fields = ['name', 'owner_name', 'location', 'total_area']


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'area', 'soil_type', 'irrigation_type']


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'season', 'duration_days']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type', 'purchase_date', 'status']