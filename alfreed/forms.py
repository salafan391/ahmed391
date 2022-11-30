from django.forms import *
from .models import *


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        exclude = ['income', 'receipiant', 'outcome', 'type', 'person']
        labels = {
            'worker': 'اسم المشتري',
            'products': 'البضاعة',
            'quantity': 'الكمية',
            'paid': 'قيمة البضاعة',
            'date_created': 'تاريخ ووقت الشراء',
        }
        widgets = {
            
            'products':TextInput(attrs={}),
            'quantity':NumberInput(attrs={}),
            'paid':NumberInput(attrs={}),
            'date_created': DateTimeInput(attrs={'type': 'datetime-local'})
        }


class IncomeForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['income', 'receipiant']
        labels = {
            'income': 'الدخل',
            'receipiant': 'المستلم',

        }
        widgets={
            'income':NumberInput(attrs={}),
        }


class OutcomeForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['outcome', 'type', 'person']
        labels = {
            'outcome': 'الخرج',
            'type': 'نوع الخرج',
            'person': 'اسم المخرج',
        }
        widgets={
            'outcome':NumberInput(attrs={}),
            'type':TextInput(attrs={})
        }
class UpdateSalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        