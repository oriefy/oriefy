from django.db import models
from contacts.models import Contact


PRECISION = getattr(settings, 'LEDGER_PRECISION', {'max_digits':12, 'decimal_places':2})

# Create your models here.
class Account(models.Model):
    """
    The ledger account linked with contacts
    """
    person = models.ForeignKey(Contact, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

