# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Debtor, Debt

def debtor_list(request):
    debtors = Debtor.objects.all()
    return render(request, 'debt_tracker/debtor_list.html', {'debtors':debtors})
