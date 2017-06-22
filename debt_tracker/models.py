# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.shortcuts import redirect


class Debtor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    uniqueid = models.IntegerField()
    add_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class Debt(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_added =  models.DateTimeField(default=timezone.now)
    owed_to = models.CharField(max_length=100)
    status = models.CharField(max_length=15, default='Not Paid')

    def pay(self, payment):
        self.amount = self.amount - payment
        if self.amount == 0:
            status = 'paid'

    def __str__(self):
        return "owes ${0} to {1}".format(self.amount, self.owed_to)

# Create your models here.
