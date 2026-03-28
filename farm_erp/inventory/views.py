from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, StockIn, StockOut
from .forms import InventoryItemForm, StockInForm, StockOutForm
from accounts.decorators import role_required


@role_required(['admin', 'manager', 'storekeeper'])
def inventory_dashboard(request):
    items = InventoryItem.objects.all()
    stock_in = StockIn.objects.all()
    stock_out = StockOut.objects.all()

    context = {
        'item_count': items.count(),
        'stock_in_count': stock_in.count(),
        'stock_out_count': stock_out.count(),
    }

    return render(request, 'inventory/inventory_dashboard.html', context)


@role_required(['admin', 'manager', 'storekeeper'])
def item_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})


@role_required(['admin', 'manager', 'storekeeper'])
def add_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/item_form.html', {'form': form, 'title': 'Add Inventory Item'})


@role_required(['admin', 'manager', 'storekeeper'])
def edit_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form, 'title': 'Edit Inventory Item'})


@role_required(['admin'])
def delete_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_delete.html', {'item': item})


@role_required(['admin', 'manager', 'storekeeper'])
def stock_in_list(request):
    records = StockIn.objects.all()
    return render(request, 'inventory/stock_in_list.html', {'records': records})


@role_required(['admin', 'manager', 'storekeeper'])
def add_stock_in(request):
    if request.method == 'POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_in_list')
    else:
        form = StockInForm()
    return render(request, 'inventory/stock_in_form.html', {'form': form, 'title': 'Add Stock In'})


@role_required(['admin', 'manager', 'storekeeper'])
def edit_stock_in(request, pk):
    record = get_object_or_404(StockIn, pk=pk)
    if request.method == 'POST':
        form = StockInForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('stock_in_list')
    else:
        form = StockInForm(instance=record)
    return render(request, 'inventory/stock_in_form.html', {'form': form, 'title': 'Edit Stock In'})


@role_required(['admin'])
def delete_stock_in(request, pk):
    record = get_object_or_404(StockIn, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('stock_in_list')
    return render(request, 'inventory/stock_in_delete.html', {'record': record})


@role_required(['admin', 'manager', 'storekeeper'])
def stock_out_list(request):
    records = StockOut.objects.all()
    return render(request, 'inventory/stock_out_list.html', {'records': records})


@role_required(['admin', 'manager', 'storekeeper'])
def add_stock_out(request):
    if request.method == 'POST':
        form = StockOutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_out_list')
    else:
        form = StockOutForm()
    return render(request, 'inventory/stock_out_form.html', {'form': form, 'title': 'Add Stock Out'})


@role_required(['admin', 'manager', 'storekeeper'])
def edit_stock_out(request, pk):
    record = get_object_or_404(StockOut, pk=pk)
    if request.method == 'POST':
        form = StockOutForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('stock_out_list')
    else:
        form = StockOutForm(instance=record)
    return render(request, 'inventory/stock_out_form.html', {'form': form, 'title': 'Edit Stock Out'})


@role_required(['admin'])
def delete_stock_out(request, pk):
    record = get_object_or_404(StockOut, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('stock_out_list')
    return render(request, 'inventory/stock_out_delete.html', {'record': record})