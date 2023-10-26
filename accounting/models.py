from django.db import models

# Create your models here.

class chartAccounts(models.Model):
    name            =   models.CharField(max_length=100, blank=True, null=True)
    type            =   models.CharField(max_length=100, blank=True, null=True)
    referenceNum    =   models.BigIntegerField(blank=True, null=True)
    balanceUSD      =   models.BigIntegerField(blank=True, null=True)
    currency        =   models.CharField(max_length=100, blank=True, null=True)
    parentAccount   =   models.CharField(max_length=100, blank=True, null=True)

class ItemServices(models.Model):
    code            =   models.CharField(max_length=100, blank=True, null=True)
    description     =   models.CharField(max_length=200, blank=True, null=True)
    accountName     =   models.CharField(max_length=200, blank=True, null=True)
    type            =   models.CharField(max_length=100, blank=True, null=True)
    amount          =   models.FloatField(blank=True, null=True)
    autCreation     =   models.CharField(max_length=100, blank=True, null=True)
    currency        =   models.CharField(max_length=100, blank=True, null=True)
    iataCode        =   models.CharField(max_length=100, blank=True, null=True)
  
class openingBalance(models.Model):
    name            =   models.CharField(max_length=100, blank=True, null=True)
    balance         =   models.FloatField(blank=True, null=True)