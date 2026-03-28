from django.urls import path
from . import views

urlpatterns = [
    path('', views.labor_dashboard, name='labor_dashboard'),

    path('workers/', views.worker_list, name='worker_list'),
    path('workers/add/', views.add_worker, name='add_worker'),
    path('workers/edit/<int:pk>/', views.edit_worker, name='edit_worker'),
    path('workers/delete/<int:pk>/', views.delete_worker, name='delete_worker'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
]