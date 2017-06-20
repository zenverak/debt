# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Debtor, Debt

# Register your models here.
admin.site.register(Debtor)
admin.site.register(Debt)

