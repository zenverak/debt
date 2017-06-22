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
        print "self.amount is {0}".format(self.amount)
        if self.amount == 0.0 or self.amount == 0:
            print "going to make status paid"
            self.status = 'paid'

    def __str__(self):
        return "owes ${0} to {1}".format(self.amount, self.owed_to)


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    business_type = models.CharField(max_length=30)


    def __str__(self):
        return "{0} Specializes in {1}".format(self.name, self.business_type)

# Create your models here.
