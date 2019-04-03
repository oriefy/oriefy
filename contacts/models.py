from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    model for contacts
    """
    name    = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=False)
    

    def __str__(self):
        return self.name