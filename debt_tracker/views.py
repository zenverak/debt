# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Debtor, Debt
from .forms import DebtPay,DebtForm, DebtorForm

def debtor_list(request):
    debtors = Debtor.objects.all()
    return render(request, 'debt_tracker/debtor_list.html', {'debtors':debtors})


def debt_list(request, id):
    '''
    Will return a dictionary containing 
    debtor and his debts
    '''
    debtor = Debtor.objects.get(uniqueid=id)
    debts = Debt.objects.filter(debtor=debtor).filter(status='Not Paid')
    info={"debtor":debtor,"debts":debts}
    return render(request, 'debt_tracker/debt_list.html',{'info':info})
	

	
def debt_pay(request,pk):
#    print request
#    print "post is {0}".format(request.POST)
#    print request.POST['payment_amount']
#    print "PAYING SOME DEBT"
    debt = Debt.objects.get(pk=pk)
    if request.method == "POST":
        debt.pay(float(request.POST['payment_amount']))
        debt.save()
#        print debt.amount
        form = DebtPay(initial={'amount':debt.amount})
        form.fields['amount'].disabled = True
        info = {"form":form, "debt":debt}
        return render(request, 'debt_tracker/debt_pay.html', {'info': info})
    else:
        form = DebtPay(initial={'amount':debt.amount})
        form.fields['amount'].disabled = True
        info = {"form":form, "debt":debt}
        return render(request, 'debt_tracker/debt_pay.html', {'info': info})

def debt_add(request, id):
    if request.method == "POST":
        form = DebtForm(request.POST)
        debt = form.save(commit=False)
        id = int(request.POST.get('id'))
        debt.debtor =  Debtor.objects.get(uniqueid=id)
        debt.save()
        return redirect('debt_list', id=debt.debtor.uniqueid)
    else:
        form = DebtForm()
        info = {'form':form, 'id':id}
        return render(request, 'debt_tracker/debt_add.html', {'info':info})

def debtor_add(request):
    if request.method == "POST":
        form = DebtorForm(request.POST)
        debtor = form.save()
        debtor.save()
        return redirect('debtor_list')
    else:
        form = DebtorForm()
        return render(request, 'debt_tracker/debtor_add.html', {'form': form})
        
    