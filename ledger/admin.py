from django.contrib import admin
from ledger.models import Account, Transaction

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    '''Admin View for Account'''

    list_display = ('person', 'balance')

    raw_id_fields = ('person',)
    search_fields = ('person__name',)
    readonly_fields = ('balance', )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''

    list_display = (
        'account',
        'amount',
        'transaction_type',
        )
    list_filter = ('transaction_type', 'account')
    raw_id_fields = ('account',)
    search_fields = ('account', 'description')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)