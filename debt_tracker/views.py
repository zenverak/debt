# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Debtor, Debt

def debtor_list(request):
    debtors = Debtor.objects.all()
    return render(request, 'debt_tracker/debtor_list.html', {'debtors':debtors})


def debt_list(request, id):
    '''
    Will return a dictionary containing 
    debtor and his debts
    '''
    debtor = Debtor.objects.get(uniqueid=id)
    debts = Debt.objects.filter(debtor=debtor)
    info={"debtor":debtor,"debts":debts}
    return render(request, 'debt_tracker/debt_list.html',{'info':info})