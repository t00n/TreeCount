from django.db import models
from django.contrib.auth.models import User
import datetime
from uuid import uuid4


def name_for_upload(*args, **kwargs):
        return str(uuid4())


class Expense(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    description = models.CharField(max_length=500)
    amount = models.FloatField()
    creditor = models.ForeignKey(User, related_name='creditor')
    debitors = models.ManyToManyField(User, related_name='debitor')
    proof = models.FileField(blank=True, verbose_name="Proof of payment",
                             upload_to=name_for_upload)

    class Meta:
        ordering = ('-date',)


class Refund(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    amount = models.FloatField()
    creditor = models.ForeignKey(User, related_name='refund_creditor')
    debitor = models.ForeignKey(User, related_name='refund_debitor')
    proof = models.FileField(blank=True, verbose_name="Proof of payment",
                             upload_to=name_for_upload)

    class Meta:
        ordering = ('-date',)
