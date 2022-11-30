from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name= 'index'),
    path('sales',views.sales_view,name='sales'),
    path('details/<int:pk>',views.details,name='details'),
    path('update_income/<int:pk>/',views.update_income_view,name='update_income'),
    path('update_outcome/<int:pk>/',views.update_outcome_view,name='update_outcome'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('sales/update/<int:pk>/',views.update_sales_view,name='update')
  
]