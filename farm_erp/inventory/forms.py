from django import forms
from .models import InventoryItem, StockIn, StockOut


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'category', 'unit', 'quantity', 'minimum_stock']


class StockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = ['item', 'date', 'quantity', 'supplier']


class StockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = ['item', 'date', 'quantity', 'issued_to']