from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_season_dashboard, name='crop_season_dashboard'),

    path('seasons/', views.season_list, name='season_list'),
    path('seasons/add/', views.add_season, name='add_season'),
    path('seasons/edit/<int:pk>/', views.edit_season, name='edit_season'),
    path('seasons/delete/<int:pk>/', views.delete_season, name='delete_season'),

    path('field-plans/', views.field_crop_plan_list, name='field_crop_plan_list'),
    path('field-plans/add/', views.add_field_crop_plan, name='add_field_crop_plan'),
    path('field-plans/edit/<int:pk>/', views.edit_field_crop_plan, name='edit_field_crop_plan'),
    path('field-plans/delete/<int:pk>/', views.delete_field_crop_plan, name='delete_field_crop_plan'),
]