from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('store/', views.store_dashboard, name='store_dashboard'),
    path('accounts/', views.accounts_dashboard, name='accounts_dashboard'),
    path('sales/', views.sales_dashboard, name='sales_dashboard'),
    path('field/', views.field_dashboard, name='field_dashboard'),
]