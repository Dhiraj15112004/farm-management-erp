from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('redirect/', views.role_redirect, name='role_redirect'),
    path('logout/', views.logout_view, name='logout'),

    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),
]