from django.contrib import admin
from contacts.models import Contact
from ledger.admin import ledger_admin_site

# Register your models here.

admin.site.register(Contact)
ledger_admin_site.register(Contact)