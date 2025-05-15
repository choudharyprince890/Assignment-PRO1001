from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm
from datetime import date


def office_transactions_grid(request):
    transactions = list(Transaction.objects.all().order_by('date', 'id'))
    
    running_balance = 0
    for transaction in transactions:
        credit = transaction.credit if transaction.credit else 0
        debit = transaction.debit if transaction.debit else 0
        running_balance += credit - debit
        transaction.running_balance = running_balance
    transactions.reverse()

    return render(request, 'transactions_grid.html', {'transactions': transactions})





def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            credit = data['amount'] if data['transaction_type'] == 'credit' else 0
            debit = data['amount'] if data['transaction_type'] == 'debit' else 0

            Transaction.objects.create(
                date=date.today(),
                description=data['description'],
                credit=credit,
                debit=debit
            )
            return redirect('office-transactions')
    else:
        form = TransactionForm()
    
    return render(request, 'add_transactions.html', {'form': form})
