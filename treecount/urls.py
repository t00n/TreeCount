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

from .views import expense_add, ExpenseListView, balance, expense_modify

expense_list = login_required(ExpenseListView.as_view())

urlpatterns = [
    url('^$', expense_list, name='home'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^expense/add/$', expense_add, name='expense_add'),
    url(r'^expense/list/$', expense_list, name='expense_list'),
    url(r'^expense/modify/(?P<id>\d+)/$', expense_modify, name="expense_modify"),
    url(r'^balance/$', balance, name='balance'),
    url(r'^admin/', admin.site.urls),
]
