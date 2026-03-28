from django.shortcuts import render, redirect, get_object_or_404
from .models import FarmProfile, Field, Crop, Equipment
from .forms import FarmProfileForm, FieldForm, CropForm, EquipmentForm
from accounts.decorators import role_required


@role_required(['admin', 'manager'])
def master_dashboard(request):
    farm_profiles = FarmProfile.objects.all()
    fields = Field.objects.all()
    crops = Crop.objects.all()
    equipments = Equipment.objects.all()

    context = {
        'farm_profiles': farm_profiles,
        'fields': fields,
        'crops': crops,
        'equipments': equipments,
        'farm_count': farm_profiles.count(),
        'field_count': fields.count(),
        'crop_count': crops.count(),
        'equipment_count': equipments.count(),
    }
    return render(request, 'master_setup/master_dashboard.html', context)


@role_required(['admin', 'manager'])
def farm_profile_list(request):
    farm_profiles = FarmProfile.objects.all()
    return render(request, 'master_setup/farm_profile_list.html', {'farm_profiles': farm_profiles})


@role_required(['admin', 'manager'])
def add_farm(request):
    if request.method == 'POST':
        form = FarmProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_profile_list')
    else:
        form = FarmProfileForm()
    return render(request, 'master_setup/farm_form.html', {'form': form, 'title': 'Add Farm Profile'})


@role_required(['admin', 'manager'])
def edit_farm(request, pk):
    farm = get_object_or_404(FarmProfile, pk=pk)
    if request.method == 'POST':
        form = FarmProfileForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm_profile_list')
    else:
        form = FarmProfileForm(instance=farm)
    return render(request, 'master_setup/farm_form.html', {'form': form, 'title': 'Edit Farm Profile'})


@role_required(['admin', 'manager'])
def delete_farm(request, pk):
    farm = get_object_or_404(FarmProfile, pk=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm_profile_list')
    return render(request, 'master_setup/farm_delete.html', {'farm': farm})


@role_required(['admin', 'manager'])
def field_list(request):
    fields = Field.objects.all()
    return render(request, 'master_setup/field_list.html', {'fields': fields})


@role_required(['admin', 'manager'])
def add_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = FieldForm()
    return render(request, 'master_setup/field_form.html', {'form': form, 'title': 'Add Field'})


@role_required(['admin', 'manager'])
def edit_field(request, pk):
    field = get_object_or_404(Field, pk=pk)
    if request.method == 'POST':
        form = FieldForm(request.POST, instance=field)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = FieldForm(instance=field)
    return render(request, 'master_setup/field_form.html', {'form': form, 'title': 'Edit Field'})


@role_required(['admin', 'manager'])
def delete_field(request, pk):
    field = get_object_or_404(Field, pk=pk)
    if request.method == 'POST':
        field.delete()
        return redirect('field_list')
    return render(request, 'master_setup/field_delete.html', {'field': field})


@role_required(['admin', 'manager'])
def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'master_setup/crop_list.html', {'crops': crops})


@role_required(['admin', 'manager'])
def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm()
    return render(request, 'master_setup/crop_form.html', {'form': form, 'title': 'Add Crop'})


@role_required(['admin', 'manager'])
def edit_crop(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm(instance=crop)
    return render(request, 'master_setup/crop_form.html', {'form': form, 'title': 'Edit Crop'})


@role_required(['admin', 'manager'])
def delete_crop(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        crop.delete()
        return redirect('crop_list')
    return render(request, 'master_setup/crop_delete.html', {'crop': crop})


@role_required(['admin', 'manager'])
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'master_setup/equipment_list.html', {'equipments': equipments})


@role_required(['admin', 'manager'])
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'master_setup/equipment_form.html', {'form': form, 'title': 'Add Equipment'})


@role_required(['admin', 'manager'])
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'master_setup/equipment_form.html', {'form': form, 'title': 'Edit Equipment'})


@role_required(['admin', 'manager'])
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'master_setup/equipment_delete.html', {'equipment': equipment})