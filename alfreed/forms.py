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

            'products': TextInput(attrs={'class': "form-label", 'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': "form-label",'class':'range'}),
            'paid': NumberInput(attrs={'class': "form-label",'class':'range'}),
            'date_created': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control"}),
            'worker':SelectMultiple(attrs={'class': "form-label", 'class': 'form-control'})
        }


class IncomeForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['income', 'receipiant']
        labels = {
            'income': 'مبلغ الدخل',
            'receipiant': 'المستلم',

        }
        widgets = {
            'income': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'receipiant':SelectMultiple(attrs={'class': "form-label",'class': 'form-control'})
        }


class OutcomeForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['outcome', 'type', 'person']
        labels = {
            'outcome': 'مبلغ الخرج',
            'type': 'نوع الخرج',
            'person': 'اسم المخرج',
        }
        widgets = {
            'outcome': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'type': TextInput(attrs={'class': "form-label", 'class': 'form-control'}),
            'person':SelectMultiple(attrs={'class':"form-label", 'class':'form-control'})
        }


class UpdateSalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        labels = {
            'worker': 'اسم المشتري',
            'products': 'البضاعة',
            'quantity': 'الكمية',
            'paid': 'قيمة البضاعة',
            'date_created': 'تاريخ ووقت الشراء',
            'income': 'مبلغ الدخل',
            'receipiant': 'المستلم',
            'outcome': 'مبلغ الخرج',
            'type': 'نوع الخرج',
            'person': 'اسم المخرج',
        }
        widgets = {
            'products': TextInput(attrs={'class': "form-label", 'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'paid': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'date_created': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control"}),
            'income': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'outcome': NumberInput(attrs={'class': "form-label",'class': 'form-control'}),
            'type': TextInput(attrs={'class': "form-label", 'class': 'form-control'}),
            'person':SelectMultiple(attrs={'class':"form-label", 'class':'form-control'}),
            'receipiant':SelectMultiple(attrs={'class': "form-label",'class': 'form-control'}),
            'worker':SelectMultiple(attrs={'class': "form-label",'class':"form-select"})


        }
