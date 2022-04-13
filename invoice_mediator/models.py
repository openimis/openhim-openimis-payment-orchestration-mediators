from django.db import models
from group_mediator.models import Group
from patient_mediator.models import Person


class Group_Account(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True,
         verbose_name ='Group AccountID')
    accountNo = models.CharField(max_length=45)
    externalID = models.CharField(max_length=45)
    productName = models.CharField(max_length=255)
    group = models.ForeignKey(Group, models.PROTECT,
        default=1, verbose_name ='Group')

    class Meta:
        managed = True
        db_table = 'account_group'
        verbose_name = 'Group Account'
        verbose_name_plural = 'Group Accounts'
        
    def __str__(self):
        return self.productName


class Personal_Account(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True,
         verbose_name ='Personal AccountID')
    accountNo = models.CharField(max_length=45)
    externalID = models.CharField(max_length=45)
    clientID = models.PositiveSmallIntegerField(verbose_name ='Client ID',default=1)
    clientName = models.CharField(max_length=45,null=True,blank=True)
    # person = models.ForeignKey(Person, models.PROTECT,
    #     default=1, verbose_name ='Person')

    class Meta:
        managed = True
        db_table = 'account_personal'
        verbose_name = 'Personal Account'
        verbose_name_plural = 'Personal Accounts'
        
    def __str__(self):
        return self.clientName # to confirm later


class Billing_Invoice(models.Model):
    id = models.AutoField(primary_key=True,
         verbose_name ='InvoiceID')
    invoiceID = models.CharField(max_length=100,unique=True)      
    client_uuid = models.CharField(max_length=45)
    invoice_issuer = models.CharField(max_length=255)
    # mifos_clientid = models.ForeignKey(Person, models.PROTECT,
    #     default=1, verbose_name ='Mifos ClientID')

    mifos_clientid = models.PositiveSmallIntegerField(default=1, 
        verbose_name ='Mifos ClientID')

    status = models.CharField(max_length=45)
    date_issued= models.DateField(blank=True, null=True)
    totalNet= models.DecimalField(max_digits=20,
        decimal_places=2,blank=False, null=False,
        default=0.00,verbose_name ='Net Amount')
    totalGross= models.DecimalField(max_digits=20,
        decimal_places=2,blank=False,null=False,
        default=0.00,verbose_name ='Gross Amount')  
    
    class Meta:
        managed = True
        db_table = 'account_invoice'
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        
    def __str__(self):
        return self.invoice_issuer # to confirm later