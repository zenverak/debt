# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def debtor_list(request):
    return render(request, 'debt_tracker/debtor_list.html', {})
