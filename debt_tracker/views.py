# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Debtor, Debt

def debtor_list(request):
    debtors = Debtor.objects.all()
    return render(request, 'debt_tracker/debtor_list.html', {'debtors':debtors})


def debt_list(request, debtor):
    debts = Debt.object.filter(debt__debtor=debtor)
    return render(request, 'debt_tracker/debts_list.html',{'debts':debts})
