from django.shortcuts import render
from accounts.decorators import role_required

from master_setup.models import FarmProfile, Field, Crop
from crop_season.models import Season, FieldCropPlan
from labor.models import Worker, Attendance, LaborTask
from machinery.models import Equipment as MachineEquipment, UsageLog, Maintenance
from inventory.models import InventoryItem, StockIn, StockOut
from finance.models import Expense, Income
from sales.models import Harvest, Sale


@role_required(['admin'])
def admin_dashboard(request):
    total_expense = sum(exp.amount for exp in Expense.objects.all())
    total_income = sum(inc.amount for inc in Income.objects.all())

    context = {
        'farm_count': FarmProfile.objects.count(),
        'field_count': Field.objects.count(),
        'crop_count': Crop.objects.count(),
        'season_count': Season.objects.count(),
        'plan_count': FieldCropPlan.objects.count(),
        'worker_count': Worker.objects.count(),
        'attendance_count': Attendance.objects.count(),
        'task_count': LaborTask.objects.count(),
        'machine_count': MachineEquipment.objects.count(),
        'usage_count': UsageLog.objects.count(),
        'maintenance_count': Maintenance.objects.count(),
        'inventory_count': InventoryItem.objects.count(),
        'stock_in_count': StockIn.objects.count(),
        'stock_out_count': StockOut.objects.count(),
        'expense_count': Expense.objects.count(),
        'income_count': Income.objects.count(),
        'harvest_count': Harvest.objects.count(),
        'sales_count': Sale.objects.count(),
        'total_expense': total_expense,
        'total_income': total_income,
        'profit': total_income - total_expense,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


@role_required(['admin', 'manager'])
def manager_dashboard(request):
    return render(request, 'dashboard/manager_dashboard.html')


@role_required(['admin', 'manager', 'supervisor'])
def supervisor_dashboard(request):
    return render(request, 'dashboard/supervisor_dashboard.html')


@role_required(['admin', 'storekeeper'])
def store_dashboard(request):
    return render(request, 'dashboard/store_dashboard.html')


@role_required(['admin', 'accountant'])
def accounts_dashboard(request):
    return render(request, 'dashboard/accounts_dashboard.html')


@role_required(['admin', 'accountant', 'sales'])
def sales_dashboard(request):
    return render(request, 'dashboard/sales_dashboard.html')


@role_required(['admin', 'field_staff'])
def field_dashboard(request):
    return render(request, 'dashboard/field_dashboard.html')