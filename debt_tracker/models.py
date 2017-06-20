# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Debtor(models.Model):
    debtor = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    add_date = models.DateTimeField(default=timezone.now)
    uniqueid = models.IntegerField()

    def __str__(self):
        return self.debtor
class Debt(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_added =  models.DateTimeField(default=timezone.now)
    owed_to = models.CharField(max_length=100)

# Create your models here.
