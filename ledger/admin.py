from django.contrib import admin
from ledger.models import Account, Transaction
from django.contrib.admin import site
# Register your models here.

class LedgerAdminSite(admin.AdminSite):
    """
    Seperate Admin Site for Ledgers models
    """
    site_header = "Oriefy Finance Team Admin"
    site_title = "Oriefy Finance Team Admin Portal"
    index_title = "Welcome to Oriefy Finance Manager Portal"

ledger_admin_site = LedgerAdminSite(name='ledger_admin')





@admin.register(Account, site=ledger_admin_site)
@admin.register(Account, site=site)
class AccountAdmin(admin.ModelAdmin):
    '''Admin View for Account'''

    list_display = ('person', 'balance')

    raw_id_fields = ('person',)
    search_fields = ('person__name',)
    readonly_fields = ('balance', )


@admin.register(Transaction, site=ledger_admin_site)
@admin.register(Transaction, site=site)
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