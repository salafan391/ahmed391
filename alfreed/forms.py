from django.forms import *
from .models import *


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        labels = {
            'worker':'اسم المشتري',
            'products':'البضاعة',
            'quantity':'الكمية',
            'paid':'قيمة البضاعة',
            'date_created':'تاريخ ووقت الشراء'
        }
        widgets={
            'date_created':DateTimeInput(attrs={'type':'datetime-local'})
        }


class IncomeForm(ModelForm):
    class Meta:
        model = Incomes
        fields = '__all__'
        labels = {
            'income':'الدخل',
            'receipiant':'المستلم',
            'sales':'البضاعة',
        }
        
class OutcomeForm(ModelForm):
    class Meta:
        model = Outcomes
        fields = '__all__'
        labels = {
            'outcome':'الخرج',
            'type':'نوع الخرج',
            'person':'اسم المخرج',
            'sales':'البضاعة'
        }
