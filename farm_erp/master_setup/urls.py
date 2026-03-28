from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_dashboard, name='master_dashboard'),

    path('farm-profiles/', views.farm_profile_list, name='farm_profile_list'),
    path('farm-profiles/add/', views.add_farm, name='add_farm'),
    path('farm-profiles/edit/<int:pk>/', views.edit_farm, name='edit_farm'),
    path('farm-profiles/delete/<int:pk>/', views.delete_farm, name='delete_farm'),

    path('fields/', views.field_list, name='field_list'),
    path('fields/add/', views.add_field, name='add_field'),
    path('fields/edit/<int:pk>/', views.edit_field, name='edit_field'),
    path('fields/delete/<int:pk>/', views.delete_field, name='delete_field'),

    path('crops/', views.crop_list, name='crop_list'),
    path('crops/add/', views.add_crop, name='add_crop'),
    path('crops/edit/<int:pk>/', views.edit_crop, name='edit_crop'),
    path('crops/delete/<int:pk>/', views.delete_crop, name='delete_crop'),

    path('equipments/', views.equipment_list, name='equipment_list'),
    path('equipments/add/', views.add_equipment, name='add_equipment'),
    path('equipments/edit/<int:pk>/', views.edit_equipment, name='edit_equipment'),
    path('equipments/delete/<int:pk>/', views.delete_equipment, name='delete_equipment'),
]