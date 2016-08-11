from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from collections import defaultdict

from .forms import ExpenseForm
from .models import Expense


@login_required
def expense_add(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ExpenseForm()
    return render(request, "expense_add.html", {'form': form})


@login_required
def expense_modify(request, id):
    if request.method == "POST":
        expense = get_object_or_404(Expense, pk=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        expense = get_object_or_404(Expense, pk=id)
        form = ExpenseForm(instance=expense)
    return render(request, "expense_modify.html", {'form': form, 'expense': expense})


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 42
    template_name = 'expense_list.html'


@login_required
def balance(request):
    expenses = Expense.objects.all().prefetch_related('creditor').prefetch_related('debitors')
    balance = defaultdict(lambda: 0)
    for expense in expenses:
        amount_due = expense.amount / len(expense.debitors.all())
        balance[expense.creditor.username] += expense.amount
        for debitor in expense.debitors.all():
            balance[debitor.username] -= amount_due
    balance = dict(balance)
    return render(request, "balance.html", {'balance': balance})
