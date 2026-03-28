from django.shortcuts import render, redirect, get_object_or_404
from .models import Season, FieldCropPlan
from .forms import SeasonForm, FieldCropPlanForm
from accounts.decorators import role_required


@role_required(['admin', 'manager', 'supervisor'])
def crop_season_dashboard(request):
    seasons = Season.objects.all()
    field_plans = FieldCropPlan.objects.all()

    context = {
        'seasons': seasons,
        'field_plans': field_plans,
        'season_count': seasons.count(),
        'field_plan_count': field_plans.count(),
    }
    return render(request, 'crop_season/crop_season_dashboard.html', context)


@role_required(['admin', 'manager', 'supervisor'])
def season_list(request):
    seasons = Season.objects.all()
    return render(request, 'crop_season/season_list.html', {'seasons': seasons})


@role_required(['admin', 'manager'])
def add_season(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm()
    return render(request, 'crop_season/season_form.html', {'form': form, 'title': 'Add Season'})


@role_required(['admin', 'manager'])
def edit_season(request, pk):
    season = get_object_or_404(Season, pk=pk)
    if request.method == 'POST':
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm(instance=season)
    return render(request, 'crop_season/season_form.html', {'form': form, 'title': 'Edit Season'})


@role_required(['admin'])
def delete_season(request, pk):
    season = get_object_or_404(Season, pk=pk)
    if request.method == 'POST':
        season.delete()
        return redirect('season_list')
    return render(request, 'crop_season/season_delete.html', {'season': season})


@role_required(['admin', 'manager', 'supervisor'])
def field_crop_plan_list(request):
    field_plans = FieldCropPlan.objects.all()
    return render(request, 'crop_season/field_crop_plan_list.html', {'field_plans': field_plans})


@role_required(['admin', 'manager'])
def add_field_crop_plan(request):
    if request.method == 'POST':
        form = FieldCropPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_crop_plan_list')
    else:
        form = FieldCropPlanForm()
    return render(request, 'crop_season/field_crop_plan_form.html', {'form': form, 'title': 'Add Field Crop Plan'})


@role_required(['admin', 'manager'])
def edit_field_crop_plan(request, pk):
    field_plan = get_object_or_404(FieldCropPlan, pk=pk)
    if request.method == 'POST':
        form = FieldCropPlanForm(request.POST, instance=field_plan)
        if form.is_valid():
            form.save()
            return redirect('field_crop_plan_list')
    else:
        form = FieldCropPlanForm(instance=field_plan)
    return render(request, 'crop_season/field_crop_plan_form.html', {'form': form, 'title': 'Edit Field Crop Plan'})


@role_required(['admin'])
def delete_field_crop_plan(request, pk):
    field_plan = get_object_or_404(FieldCropPlan, pk=pk)
    if request.method == 'POST':
        field_plan.delete()
        return redirect('field_crop_plan_list')
    return render(request, 'crop_season/field_crop_plan_delete.html', {'field_plan': field_plan})