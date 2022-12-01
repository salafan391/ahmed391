from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
    products = Sales.objects.all()[:3]
    return render(request,'alfreed/index.html',{
        'products':products,
        })

def sales_view(request):
    form = SalesForm()
    if request.method == 'POST':
        form= SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'alfreed/sales.html',{'form':form})

def update_income_view(request,pk):
    income = Sales.objects.get(pk=pk)
    form = IncomeForm(instance=income)
    if request.method == 'POST':
        form = IncomeForm(request.POST,instance=income)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'alfreed/income_form.html',{'form':form})

def update_outcome_view(request,pk):
    outcome = Sales.objects.get(pk=pk)
    form = OutcomeForm(instance=outcome)
    if request.method == 'POST':
        form = OutcomeForm(request.POST,instance=outcome)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'alfreed/outcome_form.html',{'form':form})


def details(request,pk):
    product = Sales.objects.get(pk=pk)
    buyer = product.worker.all()
    return render(request,'alfreed/details.html',{
        'product':product,
        'workers':buyer,
        })
def delete(request,pk):
    delete = Sales.objects.get(pk=pk)
    if request.method == 'POST':
        delete.delete()
        return redirect('index')
    return render(request,'alfreed/delete.html',{'delete':delete})
def update_sales_view(request,pk):
    sales = Sales.objects.get(pk=pk)
    form = UpdateSalesForm(instance=sales)
    if request.method == 'POST':
        form = UpdateSalesForm(request.POST,instance=sales)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'alfreed/outcome_form.html',{'form':form})