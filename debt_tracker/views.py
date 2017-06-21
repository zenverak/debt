# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Debtor, Debt
from .forms import DebtPay

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
	

	
def debt_pay(request,pk):
    print "PAYING SOME DEBT"
    debt = Debt.objects.get(pk=pk)
    if request.method == "POST":
#        print "THAT METHOD WAS A POST"
        form = DebtPay(request.POST)
        form.fields['amount'].disabled = True
        info = {"form":form, "debt":debt}
#        print "THE FORM BEING VALID IS {0}".format(form.is_valid())
        if form.is_valid():
#            print "form is valid"
            payment_amount = form.cleaned_data.get('payment_amount')
#            print "payment amount is {0} and current debt amount is {1}".format(payment_amount,info['debt'].amount)
            debt.pay(payment_amount)
#            print "new debt amount is {0}".format(info['debt'].amount)
            intial = {'amount': debt.amount, 'payment_amount': 0.0}
            form = DebtPay(request.POST, initial=initial)
            return render(request, 'debt_tracker/debt_pay.html', {'info': info})
        else:
            return render(request, 'debt_tracker/debt_pay.html', {'info': info})
    else:
        form = DebtPay(initial={'amount':debt.amount})
        form.fields['amount'].disabled = True
        info = {"form":form, "debt":debt}
        return render(request, 'debt_tracker/debt_pay.html', {'info': info})