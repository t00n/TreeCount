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

def compute_balance(expenses):
    balance = defaultdict(lambda: 0)
    for expense in expenses:
        amount_due = expense.amount / len(expense.debitors.all())
        balance[expense.creditor.username] += expense.amount
        for debitor in expense.debitors.all():
            balance[debitor.username] -= amount_due
    return dict(balance)

def compute_balance_solution(balance):
    def get_negative(balance):
        for k, v in balance.items():
            if v < 0:
                return k
        return None
    def get_positive(balance):
        for k, v in balance.items():
            if v > 0:
                return k
        return None
    solution = defaultdict(lambda: defaultdict(lambda: 0))
    while True:
        cred = get_positive(balance)
        deb = get_negative(balance)
        if cred == None or deb == None:
            break
        amount = min(-balance[deb], balance[cred])
        solution[deb][cred] += amount
        balance[deb] += amount
        balance[cred] -= amount
    return {k: dict(v) for k, v in solution.items()}


@login_required
def balance(request):
    expenses = Expense.objects.all().prefetch_related('creditor').prefetch_related('debitors')
    balance = compute_balance(expenses)
    return render(request, "balance.html", {'balance': balance})

@login_required
def balance_solution(request):
    expenses = Expense.objects.all().prefetch_related('creditor').prefetch_related('debitors')
    balance = compute_balance(expenses)
    balance_solution = compute_balance_solution(balance)
    return render(request, "balance_solution.html", {'balance_solution': balance_solution})