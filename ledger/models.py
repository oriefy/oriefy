from django.db import models
from contacts.models import Contact
from django.utils import timezone
from django.shortcuts import get_object_or_404


DENE = 'dene'
LENE = 'lene'
PAID = 'paid'
RECIEVED = 'recv'


TRANSACTION_TYPES = (
    (DENE, 'Dene Hen'),
    (LENE, 'Lene Hen'),
    (PAID, 'Paid'),
    (RECIEVED, 'Recieved')
)

# Create your models here.
class Account(models.Model):
    """
    The ledger account linked with contacts
    """
    person = models.ForeignKey(Contact, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    

    def __str__(self):
        return self.person.name



class Transaction(models.Model):
    """
    Transaction for the account
    2 types of transaction
    debit and credit
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount  = models.PositiveIntegerField(default=0)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.account.__str__()

    def save(self, *args, **kwargs):
        """
        update the balance of the account before saving the transaction
        """
        account = get_object_or_404(Account, pk=self.account.pk)
        if self.transaction_type in (PAID, LENE):
            account.balance = account.balance-self.amount
            account.save()
        else:
            account.balance = account.balance+self.amount
            account.save()
        super(Transaction, self).save(*args, **kwargs)
