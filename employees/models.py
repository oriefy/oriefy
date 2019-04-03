from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.pk, filename)


# Create your models here.
class Employee(models.Model):
    """
    Employee Profile Model
    Links to User model
    """

    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    picture             = models.ImageField('Profile Picture', upload_to=user_directory_path)
    temporary_address   = models.CharField('Temporary Address', max_length=200)
    permanent_address   = models.CharField('Permanent Address', max_length=200)
    linkdin_url        = models.URLField('Linkdin URL', max_length=60)
    facebook_url        = models.URLField('Facebook URL', max_length=60, blank=True)
    github_url          = models.URLField('Github URL', max_length=60, blank=True)
    #Guardian
    father_name         = models.CharField(max_length=50)
    father_cnic         = models.CharField(max_length=13)
    fathers_phone_no    = models.CharField(max_length=11, default="0000000")

    #verification
    verified            = models.BooleanField('Verified', default=False)
    





def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 




class EducationRecord(models.Model):
    """
    Save Education record of an employee
    """

    employee        = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    year            = models.IntegerField(
        validators=[MinValueValidator(2000),
        max_value_current_year])
    total_marks     = models.PositiveIntegerField()
    obtained_marks  = models.PositiveIntegerField()


RecordCategoryChoices = (
    ("cnic", "CNIC"),
    ("domicile", "Domicile"),
    ("metric", "Metric Certificate"),
    ("intermediate", "Intermediate Certificate"),
    ("graduation", "Graduation Certificate"),
    ("other", "Other Documents")
)


def employee_certificates_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/certs/{1}'.format(instance.user.pk, filename)



class RecordImage(models.Model):
    """
    For photos of certificates
    """
    employee        = models.ForeignKey(Employee, on_delete=models.CASCADE)
    category        = models.CharField(max_length=15, choices=RecordCategoryChoices)
    image           = models.ImageField('Document Photo', upload_to=employee_certificates_path)


class PhoneNumber(models.Model):
    """
    Saves phone numbers of users
    """
    person      = models.ForeignKey(User, on_delete=models.CASCADE)
    number      = models.CharField(max_length=12)