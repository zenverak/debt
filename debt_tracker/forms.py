from django import forms
from .models import Debtor, Debt


class DebtorForm(forms.ModelForm):


    class Meta:
        model = Debtor
        fields = ('name', 'address', 'uniqueid')


class DebtForm(forms.ModelForm):


    class Meta:
        model = Debt
        fields = ('amount', 'owed_to',)

        
class DebtPay(forms.ModelForm):

    payment_amount = forms.FloatField()


    class Meta:
        model = Debt
        fields = ('amount', )
