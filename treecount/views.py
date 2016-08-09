from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
def index(request):
	expenses = Expense.objects.all().prefetch_related('creditors').prefetch_related('debitors')
	return render(request, "index.html", {'expenses': expenses})