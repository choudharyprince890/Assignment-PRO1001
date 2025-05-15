from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'credit', 'debit')  
    search_fields = ('description',)  
    list_filter = ('date',) 