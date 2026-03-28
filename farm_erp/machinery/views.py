from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment, UsageLog, Maintenance
from .forms import EquipmentForm, UsageLogForm, MaintenanceForm
from accounts.decorators import role_required


@role_required(['admin', 'manager'])
def machinery_dashboard(request):
    equipment = Equipment.objects.all()
    usage = UsageLog.objects.all()
    maintenance = Maintenance.objects.all()

    context = {
        'equipment_count': equipment.count(),
        'usage_count': usage.count(),
        'maintenance_count': maintenance.count(),
    }

    return render(request, 'machinery/machinery_dashboard.html', context)


@role_required(['admin', 'manager'])
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'machinery/equipment_list.html', {'equipments': equipments})


@role_required(['admin', 'manager'])
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machinery_equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'machinery/equipment_form.html', {'form': form, 'title': 'Add Equipment'})


@role_required(['admin', 'manager'])
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('machinery_equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'machinery/equipment_form.html', {'form': form, 'title': 'Edit Equipment'})


@role_required(['admin'])
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('machinery_equipment_list')
    return render(request, 'machinery/equipment_delete.html', {'equipment': equipment})


@role_required(['admin', 'manager'])
def usage_list(request):
    usages = UsageLog.objects.all()
    return render(request, 'machinery/usage_list.html', {'usages': usages})


@role_required(['admin', 'manager'])
def add_usage(request):
    if request.method == 'POST':
        form = UsageLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usage_list')
    else:
        form = UsageLogForm()
    return render(request, 'machinery/usage_form.html', {'form': form, 'title': 'Add Usage Log'})


@role_required(['admin', 'manager'])
def edit_usage(request, pk):
    usage = get_object_or_404(UsageLog, pk=pk)
    if request.method == 'POST':
        form = UsageLogForm(request.POST, instance=usage)
        if form.is_valid():
            form.save()
            return redirect('usage_list')
    else:
        form = UsageLogForm(instance=usage)
    return render(request, 'machinery/usage_form.html', {'form': form, 'title': 'Edit Usage Log'})


@role_required(['admin'])
def delete_usage(request, pk):
    usage = get_object_or_404(UsageLog, pk=pk)
    if request.method == 'POST':
        usage.delete()
        return redirect('usage_list')
    return render(request, 'machinery/usage_delete.html', {'usage': usage})


@role_required(['admin', 'manager'])
def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    return render(request, 'machinery/maintenance_list.html', {'maintenances': maintenances})


@role_required(['admin', 'manager'])
def add_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm()
    return render(request, 'machinery/maintenance_form.html', {'form': form, 'title': 'Add Maintenance'})


@role_required(['admin', 'manager'])
def edit_maintenance(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm(instance=maintenance)
    return render(request, 'machinery/maintenance_form.html', {'form': form, 'title': 'Edit Maintenance'})


@role_required(['admin'])
def delete_maintenance(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    if request.method == 'POST':
        maintenance.delete()
        return redirect('maintenance_list')
    return render(request, 'machinery/maintenance_delete.html', {'maintenance': maintenance})