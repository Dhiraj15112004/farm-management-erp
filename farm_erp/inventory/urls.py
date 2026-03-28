from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name='inventory_dashboard'),

    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:pk>/', views.delete_item, name='delete_item'),

    path('stock-in/', views.stock_in_list, name='stock_in_list'),
    path('stock-in/add/', views.add_stock_in, name='add_stock_in'),
    path('stock-in/edit/<int:pk>/', views.edit_stock_in, name='edit_stock_in'),
    path('stock-in/delete/<int:pk>/', views.delete_stock_in, name='delete_stock_in'),

    path('stock-out/', views.stock_out_list, name='stock_out_list'),
    path('stock-out/add/', views.add_stock_out, name='add_stock_out'),
    path('stock-out/edit/<int:pk>/', views.edit_stock_out, name='edit_stock_out'),
    path('stock-out/delete/<int:pk>/', views.delete_stock_out, name='delete_stock_out'),
]