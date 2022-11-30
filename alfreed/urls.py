from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name= 'index'),
    path('sales',views.sales_view,name='sales'),
    path('income',views.income_view,name='income'),
    path('outcome',views.outcome_view,name='outcome'),
    path('details/<int:pk>',views.details,name='details'),
  
]