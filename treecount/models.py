from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
	date = models.DateField(auto_now_add=True)
	description = models.CharField(max_length=500)
	amount = models.FloatField()
	creditor = models.ForeignKey(User, related_name='creditor')
	debitors = models.ManyToManyField(User, related_name='debitor')

	class Meta:
		ordering = ('date',)