from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserForm
from .decorators import role_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('role_redirect')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('role_redirect')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


@login_required
def role_redirect(request):
    role = request.user.role

    if role == 'admin':
        return redirect('admin_dashboard')
    elif role == 'manager':
        return redirect('manager_dashboard')
    elif role == 'supervisor':
        return redirect('supervisor_dashboard')
    elif role == 'storekeeper':
        return redirect('store_dashboard')
    elif role == 'accountant':
        return redirect('accounts_dashboard')
    elif role == 'sales':
        return redirect('sales_dashboard')
    else:
        return redirect('field_dashboard')


def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- USER MANAGEMENT (ADMIN ONLY) ----------------

@role_required(['admin'])
def user_list(request):
    users = User.objects.all().order_by('id')
    return render(request, 'accounts/user_list.html', {'users': users})


@role_required(['admin'])
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'accounts/user_form.html', {
        'form': form,
        'title': 'Add User'
    })


@role_required(['admin'])
def edit_user(request, pk):
    user_obj = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user_obj)
        form.fields['password'].required = False

    return render(request, 'accounts/user_form.html', {
        'form': form,
        'title': 'Edit User'
    })


@role_required(['admin'])
def delete_user(request, pk):
    user_obj = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user_obj.delete()
        return redirect('user_list')

    return render(request, 'accounts/user_delete.html', {'user_obj': user_obj})