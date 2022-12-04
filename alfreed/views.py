from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Sales.objects.filter(
        Q(worker__name__icontains=q) |
        Q(products__icontains=q) |
        Q(type__icontains=q) |
        Q(receipiant__name__icontains=q) |
        Q(person__name__icontains=q) |
        Q(quantity__icontains=q) |
        Q(paid__icontains=q) |
        Q(date_created__icontains=q) |
        Q(income__icontains=q) |
        Q(outcome__icontains=q) |
        Q(created__icontains=q)
    ).distinct()
    
    sum = Sales.objects.filter(worker__name=q).aggregate(
        Sum('paid'), Sum('income'), Sum('outcome'))
    if sum['paid__sum'] is None or sum['income__sum'] is None or sum['outcome__sum'] is None:
        sum = Sales.objects.filter().aggregate(
            Sum('paid'), Sum('income'), Sum('outcome'))
    workers = Workers.objects.all()
    return render(request, 'alfreed/index.html',{
        'products': products,
        'workers': workers,
        'sum': sum,
    })


def sales_view(request):
    form = SalesForm()
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'alfreed/sales.html', {'form': form})


def update_income_view(request, pk):
    income = Sales.objects.get(pk=pk)
    form = IncomeForm(instance=income)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'alfreed/income_form.html', {'form': form})


def update_outcome_view(request, pk):
    outcome = Sales.objects.get(pk=pk)
    form = OutcomeForm(instance=outcome)
    if request.method == 'POST':
        form = OutcomeForm(request.POST, instance=outcome)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'alfreed/outcome_form.html', {'form': form})


def details(request, pk):
    product = Sales.objects.get(pk=pk)
    buyer = product.worker.all()
    return render(request, 'alfreed/details.html', {
        'product': product,
        'workers': buyer,
    })


def delete(request, pk):
    delete = Sales.objects.get(pk=pk)
    if request.method == 'POST':
        delete.delete()
        return redirect('index')
    return render(request, 'alfreed/delete.html', {'delete': delete})


def update_sales_view(request, pk):
    sales = Sales.objects.get(pk=pk)
    form = UpdateSalesForm(instance=sales)
    if request.method == 'POST':
        form = UpdateSalesForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'alfreed/outcome_form.html', {'form': form})


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'اسم المستخدم غير موجود')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    context = {'page': page}
    return render(request, 'alfreed/login_alfreed.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'اسم المستخدم او كلمة المرور لا تتطابق')
    return render(request, 'alfreed/login_alfreed.html', {
        'form': form
    })
