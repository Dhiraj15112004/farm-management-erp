from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_dashboard, name='sales_dashboard'),

    path('harvest/', views.harvest_list, name='harvest_list'),
    path('harvest/add/', views.add_harvest, name='add_harvest'),
    path('harvest/edit/<int:pk>/', views.edit_harvest, name='edit_harvest'),
    path('harvest/delete/<int:pk>/', views.delete_harvest, name='delete_harvest'),

    path('sale/', views.sale_list, name='sale_list'),
    path('sale/add/', views.add_sale, name='add_sale'),
    path('sale/edit/<int:pk>/', views.edit_sale, name='edit_sale'),
    path('sale/delete/<int:pk>/', views.delete_sale, name='delete_sale'),
]