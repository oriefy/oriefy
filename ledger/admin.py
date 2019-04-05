from django.contrib import admin
from ledger.models import Account, Transaction
from django.contrib.admin import site
from django.db import models
from django.forms import Textarea
from oriefy.utils import ExportCsvMixin
# Register your models here.

class LedgerAdminSite(admin.AdminSite):
    """
    Seperate Admin Site for Ledgers models
    """
    site_header = "Oriefy Finance Team Admin"
    site_title = "Oriefy Finance Team Admin Portal"
    index_title = "Welcome to Oriefy Finance Manager Portal"

ledger_admin_site = LedgerAdminSite(name='ledger_admin')


class TransactionInline(admin.TabularInline):
    '''Tabular Inline View for Transaction'''

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

    model = Transaction
    min_num = 3
    max_num = 20
    extra = 1
    fk_name = 'account'
    radio_fields = {'transaction_type':admin.HORIZONTAL}


@admin.register(Account, site=ledger_admin_site)
@admin.register(Account, site=site)
class AccountAdmin(admin.ModelAdmin, ExportCsvMixin):
    '''Admin View for Account'''


    list_display = ('person', 'balance')

    raw_id_fields = ('person',)
    search_fields = ('person__name',)
    readonly_fields = ('balance', )

    inlines = [
        TransactionInline,
    ]

    # Actions
    actions = ['export_to_csv']


@admin.register(Transaction, site=ledger_admin_site)
@admin.register(Transaction, site=site)
class TransactionAdmin(admin.ModelAdmin, ExportCsvMixin):
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
    radio_fields = {'transaction_type':admin.HORIZONTAL}

    # Actions
    actions = ['export_as_csv']