"""treecount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import ExpenseListView, ExpenseCreate, ExpenseUpdate, balance, balance_solution

expense_list = login_required(ExpenseListView.as_view())

urlpatterns = [
    url('^$', expense_list, name='home'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^expense/create/$', login_required(ExpenseCreate.as_view(template_name="expense_form.html")), name="expense_create"),
    url(r'^expense/list/$', expense_list, name="expense_list"),
    url(r'^expense/update/(?P<pk>\d+)/$', login_required(ExpenseUpdate.as_view(template_name="expense_form.html")), name="expense_update"),
    url(r'^balance/$', balance),
    url(r'^balance_solution/$', balance_solution),
    url(r'^admin/', admin.site.urls),
]
