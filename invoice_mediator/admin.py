from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
# # Register your models here.
from .models import Group_Account, Personal_Account,Billing_Invoice


@admin.register(Group_Account)
class GroupAccountAdmin(ImportExportModelAdmin):
    list_display = ('id','accountNo','externalID','productName','group')


@admin.register(Personal_Account)
class PersonalAccountAdmin(ImportExportModelAdmin):
    list_display = ('id','accountNo','externalID','clientID','clientName',)

@admin.register(Billing_Invoice)
class BillingInvoiceAdmin(ImportExportModelAdmin):
    list_display = ('id','invoiceID','client_uuid','mifos_clientid','invoice_issuer',
                    'status','date_issued','totalNet','totalGross',)