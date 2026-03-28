from django.urls import path
from . import views

urlpatterns = [
    path('', views.machinery_dashboard, name='machinery_dashboard'),

    path('equipments/', views.equipment_list, name='machinery_equipment_list'),
    path('equipments/add/', views.add_equipment, name='machinery_add_equipment'),
    path('equipments/edit/<int:pk>/', views.edit_equipment, name='machinery_edit_equipment'),
    path('equipments/delete/<int:pk>/', views.delete_equipment, name='machinery_delete_equipment'),

    path('usage/', views.usage_list, name='usage_list'),
    path('usage/add/', views.add_usage, name='add_usage'),
    path('usage/edit/<int:pk>/', views.edit_usage, name='edit_usage'),
    path('usage/delete/<int:pk>/', views.delete_usage, name='delete_usage'),

    path('maintenance/', views.maintenance_list, name='maintenance_list'),
    path('maintenance/add/', views.add_maintenance, name='add_maintenance'),
    path('maintenance/edit/<int:pk>/', views.edit_maintenance, name='edit_maintenance'),
    path('maintenance/delete/<int:pk>/', views.delete_maintenance, name='delete_maintenance'),
]