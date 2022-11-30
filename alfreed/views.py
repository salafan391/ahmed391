from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
    products = Sales.objects.all()
    return render(request,'forms/index.html',{
        'products':products,
        })

def sales_view(request):
    form = SalesForm()
    if request.method == 'POST':
        form= SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'forms/sales.html',{'form':form})

def income_view(request):
    form = IncomeForm()
    if request.method == 'POST':
        form= IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'forms/income.html',{'form':form})


def outcome_view(request):
    form = OutcomeForm()
    if request.method == 'POST':
        form= OutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'forms/outcome.html',{'form':form})

def details(request,pk):
    product = Sales.objects.get(pk=pk)
    buyer = product.worker.all()
    income = product.incomes_set.all()
    outcome = product.outcomes_set.all()
    form_income = IncomeForm()
    form_outcome = OutcomeForm
    return render(request,'forms/details.html',{
        'product':product,
        'workers':buyer,
        'incomes':income,
        'outcomes':outcome,
        'form_income': form_income,
        'form_outcome':form_outcome
        })
