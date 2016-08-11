from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from collections import defaultdict

from .models import Expense


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 42
    template_name = 'expense_list.html'


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['date', 'description', 'amount', 'creditor', 'debitors']
    success_url = "/expense/list"

    def get_context_data(self, **kwargs):
        context = super(ExpenseCreate, self).get_context_data(**kwargs)
        context['button_value'] = "Create"
        return context


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['date', 'description', 'amount', 'creditor', 'debitors']
    success_url = "/expense/list"

    def get_context_data(self, **kwargs):
        context = super(ExpenseUpdate, self).get_context_data(**kwargs)
        context['button_value'] = "Update"
        return context


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
