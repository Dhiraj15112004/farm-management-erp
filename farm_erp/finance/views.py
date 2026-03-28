from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm
from accounts.decorators import role_required


@role_required(['admin', 'accountant'])
def finance_dashboard(request):
    expense = Expense.objects.all()
    income = Income.objects.all()

    context = {
        'expense_count': expense.count(),
        'income_count': income.count(),
    }

    return render(request, 'finance/finance_dashboard.html', context)


@role_required(['admin', 'accountant'])
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'finance/expense_list.html', {'expenses': expenses})


@role_required(['admin', 'accountant'])
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'finance/expense_form.html', {'form': form, 'title': 'Add Expense'})


@role_required(['admin', 'accountant'])
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'finance/expense_form.html', {'form': form, 'title': 'Edit Expense'})


@role_required(['admin'])
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'finance/expense_delete.html', {'expense': expense})


@role_required(['admin', 'accountant'])
def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'finance/income_list.html', {'incomes': incomes})


@role_required(['admin', 'accountant'])
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'finance/income_form.html', {'form': form, 'title': 'Add Income'})


@role_required(['admin', 'accountant'])
def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'finance/income_form.html', {'form': form, 'title': 'Edit Income'})


@role_required(['admin'])
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'finance/income_delete.html', {'income': income})