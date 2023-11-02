from django.db import models

# Create your models here.

class chartAccounts(models.Model):
    name            =   models.CharField(max_length=100, blank=True, null=True)
    type            =   models.CharField(max_length=100, blank=True, null=True)
    referenceNum    =   models.BigIntegerField(blank=True, null=True)
    balanceUSD      =   models.BigIntegerField(blank=True, null=True)
    currency        =   models.CharField(max_length=100, blank=True, null=True)
    parentAccount   =   models.CharField(max_length=100, blank=True, null=True)
    accountNumber   =   models.CharField(max_length=100, blank=True, null=True)
    note            =   models.CharField(max_length=100, blank=True, null=True)

class ItemServices(models.Model):
    code        =   models.CharField(max_length=100, blank=True, null=True)
    description =   models.CharField(max_length=200, blank=True, null=True)
    accountName =   models.CharField(max_length=200, blank=True, null=True)
    type        =   models.CharField(max_length=100, blank=True, null=True)
    amount      =   models.FloatField(blank=True, null=True)
    autCreation =   models.CharField(max_length=100, blank=True, null=True)
    currency    =   models.CharField(max_length=100, blank=True, null=True)
    iataCode    =   models.CharField(max_length=100, blank=True, null=True)
  
class openingBalance(models.Model):
    name        =   models.CharField(max_length=100, blank=True, null=True)
    balance     =   models.FloatField(blank=True, null=True)

class invoice(models.Model):
    number      =   models.CharField(max_length=200, blank=True, null=True)
    account     =   models.CharField(max_length=200, blank=True, null=True)
    paymentTem  =   models.CharField(max_length=200, blank=True, null=True)
    division    =   models.CharField(max_length=200, blank=True, null=True)
    apply       =   models.CharField(max_length=200, blank=True, null=True)
    due         =   models.DateField(blank=True, null=True)
    trasaDate   =   models.DateField(blank=True, null=True)
    bilingAddres=   models.TextField(blank=True, null=True)
    currency    =   models.CharField(max_length=200, blank=True, null=True)
    issuedById  =   models.CharField(max_length=200, blank=True, null=True)
    issuedByName=   models.CharField(max_length=200, blank=True, null=True)

    invoiceById=   models.CharField(max_length=200, blank=True, null=True)
    invoiceBydescription=    models.CharField(max_length=200, blank=True, null=True)
    
    paymentById=   models.CharField(max_length=200, blank=True, null=True)
    paymentByDesc=    models.CharField(max_length=200, blank=True, null=True)

    # ----------------------
    paidAdd         =   models.CharField(max_length=200, blank=True, null=True)
    exchangeRate    =   models.BigIntegerField(blank=True, null=True)
    amount          =   models.BigIntegerField(blank=True, null=True)
    totalAmount     =   models.BigIntegerField(blank=True, null=True)
    invoiceCharges  =   models.JSONField(blank=True, null=True)
    taxCode         =   models.BigIntegerField(blank=True, null=True)
    amountDue       =   models.BigIntegerField(blank=True, null=True)
    charges         =   models.JSONField(blank=True, null=True)
