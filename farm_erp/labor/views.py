from django.shortcuts import render, redirect, get_object_or_404
from .models import Worker, Attendance, LaborTask
from .forms import WorkerForm, AttendanceForm, LaborTaskForm
from accounts.decorators import role_required


@role_required(['admin', 'manager', 'supervisor'])
def labor_dashboard(request):
    workers = Worker.objects.all()
    attendance = Attendance.objects.all()
    tasks = LaborTask.objects.all()

    context = {
        'worker_count': workers.count(),
        'attendance_count': attendance.count(),
        'task_count': tasks.count(),
    }

    return render(request, 'labor/labor_dashboard.html', context)


@role_required(['admin', 'manager', 'supervisor'])
def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'labor/worker_list.html', {'workers': workers})


@role_required(['admin', 'manager'])
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'labor/worker_form.html', {'form': form, 'title': 'Add Worker'})


@role_required(['admin', 'manager'])
def edit_worker(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'labor/worker_form.html', {'form': form, 'title': 'Edit Worker'})


@role_required(['admin'])
def delete_worker(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'labor/worker_delete.html', {'worker': worker})


@role_required(['admin', 'manager', 'supervisor'])
def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'labor/attendance_list.html', {'attendance': attendance})


@role_required(['admin', 'manager', 'supervisor'])
def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'labor/attendance_form.html', {'form': form, 'title': 'Add Attendance'})


@role_required(['admin', 'manager', 'supervisor'])
def edit_attendance(request, pk):
    attendance_obj = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_obj)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance_obj)
    return render(request, 'labor/attendance_form.html', {'form': form, 'title': 'Edit Attendance'})


@role_required(['admin'])
def delete_attendance(request, pk):
    attendance_obj = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance_obj.delete()
        return redirect('attendance_list')
    return render(request, 'labor/attendance_delete.html', {'attendance_obj': attendance_obj})


@role_required(['admin', 'manager', 'supervisor'])
def task_list(request):
    tasks = LaborTask.objects.all()
    return render(request, 'labor/task_list.html', {'tasks': tasks})


@role_required(['admin', 'manager', 'supervisor'])
def add_task(request):
    if request.method == 'POST':
        form = LaborTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = LaborTaskForm()
    return render(request, 'labor/task_form.html', {'form': form, 'title': 'Add Task'})


@role_required(['admin', 'manager', 'supervisor'])
def edit_task(request, pk):
    task = get_object_or_404(LaborTask, pk=pk)
    if request.method == 'POST':
        form = LaborTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = LaborTaskForm(instance=task)
    return render(request, 'labor/task_form.html', {'form': form, 'title': 'Edit Task'})


@role_required(['admin'])
def delete_task(request, pk):
    task = get_object_or_404(LaborTask, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'labor/task_delete.html', {'task': task})