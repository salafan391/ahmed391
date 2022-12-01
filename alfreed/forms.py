from django.forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'placeholder':'كلمة المرور',
            'class':'form-label',
            'class':'form-control',})
        self.fields['password2'].widget.attrs.update({
            'placeholder':'تأكيد كلمة المرور',
            'class':'form-label',
            'class':'form-control',
            
        })
    class Meta:
        model = User
        fields= ['username','first_name','last_name']
        widgets = {
            'first_name': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'الاسم الأول'}),
            'username': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'اسم المستخدم'}),
            'last_name':TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'اللقب'})
        } 
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
            'person':SelectMultiple(attrs={'class':"form-label", 'class':"form-select"}),
            'receipiant':SelectMultiple(attrs={'class': "form-label",'class': "form-select"}),
            'worker':SelectMultiple(attrs={'class': "form-label",'class':"form-select"})
        }
