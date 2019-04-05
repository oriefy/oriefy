from django.contrib import admin
from django.contrib.auth.models import User
from employees.models import Employee, EducationRecord, RecordImage, PhoneNumber

# Register your models here.



class EmployeeAdminSite(admin.AdminSite):
    """
    Seperate Admin Site for Employees models
    """
    site_header = "Oriefy Team Admin"
    site_title = "Oriefy Team Admin Portal"
    index_title = "Welcome to Oriefy Team Member Portal"

employee_admin_site = EmployeeAdminSite(name='employee_admin')


class PhoneNumberTabularInline(admin.StackedInline):
    """
    Tabuar form for phone numbers to show in Employee admin
    """
    model = PhoneNumber
    fk_name = 'person'
    extra = 1

class EducationRecordTabularInline(admin.TabularInline):
    """
    Tabuar form for phone numbers to show in Employee admin
    """
    model = EducationRecord
    fk_name = 'employee'
    extra = 1

class RecordImageTabularInline(admin.TabularInline):
    """
    Tabuar form for phone numbers to show in Employee admin
    """
    model = RecordImage
    fk_name = 'employee'
    extra = 4

@admin.register(Employee, site=employee_admin_site)
@admin.register(Employee, site=admin.site)
class EmployeeAdmin(admin.ModelAdmin):
    '''Admin View for Employee'''
    inlines = [
        PhoneNumberTabularInline,
        EducationRecordTabularInline,
        RecordImageTabularInline]

    class Meta:
        model = Employee