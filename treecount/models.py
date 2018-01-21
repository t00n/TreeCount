from django.db import models
from django.contrib.auth.models import User
import datetime


class Expense(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    description = models.CharField(max_length=500)
    amount = models.FloatField()
    creditor = models.ForeignKey(User, related_name='creditor', on_delete=models.CASCADE)
    debitors = models.ManyToManyField(User, related_name='debitor')

    class Meta:
        ordering = ('-date',)


class Refund(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    amount = models.FloatField()
    creditor = models.ForeignKey(User, related_name='refund_creditor', on_delete=models.CASCADE)
    debitor = models.ForeignKey(User, related_name='refund_debitor', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)
