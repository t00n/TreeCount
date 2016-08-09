from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from collections import defaultdict

from .forms import ExpenseForm
from .models import Expense

@login_required
def expense_create(request):
	if request.method == "POST":
		form = ExpenseForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ExpenseForm()
	return render(request, "expense_create.html", {'form': form})

@login_required
def expense_list(request):
	expenses = Expense.objects.all().prefetch_related('creditors').prefetch_related('debitors')
	return render(request, "expense_list.html", {'expenses': expenses})

@login_required
def balance(request):
	expenses = Expense.objects.all().prefetch_related('creditors').prefetch_related('debitors')
	balance = defaultdict(lambda: 0)
	for expense in expenses:
		amount_given = expense.amount / len(expense.creditors.all())
		amount_due = expense.amount / len(expense.debitors.all())
		for creditor in expense.creditors.all():
			balance[creditor.username] += amount_given
		for debitor in expense.debitors.all():
			balance[debitor.username] -= amount_due
	balance = dict(balance)
	return render(request, "balance.html", {'balance': balance})