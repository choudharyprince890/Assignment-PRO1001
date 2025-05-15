from django import forms

class TransactionForm(forms.Form):
    TRANSACTION_TYPE_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPE_CHOICES, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    description = forms.CharField(max_length=255, required=True)
