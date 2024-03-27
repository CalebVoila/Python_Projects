from django import forms
from .models import ElectricityBill

class ElectricityBillForm(forms.ModelForm):
    class Meta:
        model = ElectricityBill
        fields = ['customer', 'reading', 'amount', 'date']
