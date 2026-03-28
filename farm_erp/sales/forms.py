from django import forms
from .models import Harvest, Sale


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['crop', 'quantity', 'date']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['crop', 'buyer', 'quantity', 'amount', 'date']