from django.shortcuts import render, redirect, get_object_or_404
from .models import Harvest, Sale
from .forms import HarvestForm, SaleForm
from accounts.decorators import role_required


@role_required(['admin', 'accountant', 'sales'])
def sales_dashboard(request):
    harvest = Harvest.objects.all()
    sales = Sale.objects.all()

    context = {
        'harvest_count': harvest.count(),
        'sales_count': sales.count(),
    }

    return render(request, 'sales/sales_dashboard.html', context)


@role_required(['admin', 'accountant', 'sales'])
def harvest_list(request):
    harvests = Harvest.objects.all()
    return render(request, 'sales/harvest_list.html', {'harvests': harvests})


@role_required(['admin', 'accountant'])
def add_harvest(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('harvest_list')
    else:
        form = HarvestForm()
    return render(request, 'sales/harvest_form.html', {'form': form, 'title': 'Add Harvest'})


@role_required(['admin', 'accountant'])
def edit_harvest(request, pk):
    harvest = get_object_or_404(Harvest, pk=pk)
    if request.method == 'POST':
        form = HarvestForm(request.POST, instance=harvest)
        if form.is_valid():
            form.save()
            return redirect('harvest_list')
    else:
        form = HarvestForm(instance=harvest)
    return render(request, 'sales/harvest_form.html', {'form': form, 'title': 'Edit Harvest'})


@role_required(['admin'])
def delete_harvest(request, pk):
    harvest = get_object_or_404(Harvest, pk=pk)
    if request.method == 'POST':
        harvest.delete()
        return redirect('harvest_list')
    return render(request, 'sales/harvest_delete.html', {'harvest': harvest})


@role_required(['admin', 'accountant', 'sales'])
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})


@role_required(['admin', 'accountant', 'sales'])
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sales/sale_form.html', {'form': form, 'title': 'Add Sale'})


@role_required(['admin', 'accountant', 'sales'])
def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sales/sale_form.html', {'form': form, 'title': 'Edit Sale'})


@role_required(['admin'])
def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'sales/sale_delete.html', {'sale': sale})