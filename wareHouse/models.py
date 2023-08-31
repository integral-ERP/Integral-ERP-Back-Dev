from django.db import models

from maintenance.models import employee, forwarAgent, carrier, customer

# Create your models here.

class pickUpOrder(models.Model):
    status          =   models.CharField(max_length=200, blank=True, null=True)
    number          =   models.PositiveBigIntegerField(blank=True, null=True)
    creationDate    =   models.DateField()
    pickUpDate      =   models.DateField()
    deliveryDate    =   models.DateField()
    date            =   models.DateField()
    issuedByKey     =   models.CharField(max_length=200, blank=True, null=True)
    destinationAgentKey    =   models.ForeignKey(forwarAgent, blank=True, null=True, on_delete=models.DO_NOTHING) 
    employeekey     =   models.OneToOneField(employee, blank=True, null=True, on_delete=models.DO_NOTHING)     
    shipperkey         =   models.TextField(blank=True, null=True)
    PickUpLocationkey  =   models.TextField(blank=True, null=True)
    consigneekey       =   models.TextField(blank=True, null=True)
    deliveryLocationkey    =   models.CharField(max_length=200, blank=True, null=True)
    inlandCarrier   =   models.ForeignKey(carrier, blank=True, null=True, on_delete=models.DO_NOTHING) 
    mainCarrierKey  =   models.CharField(max_length=200, blank=True, null=True)
    proNumber       =   models.CharField(max_length=200, blank=True, null=True)
    trackingNumber  =   models.CharField(max_length=200, blank=True, null=True)
    supplierKey     =   models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING) 
    invoiceNumber   =   models.CharField(max_length=200, blank=True, null=True)
    purchaseOrderNum    =   models.CharField(max_length=200, blank=True, null=True)
    

class pieces(models.Model):
    status      =   models.FloatField(blank=True, null=True, default=0) 
    package     =   models.FloatField(blank=True, null=True, default=0) 
    description =   models.FloatField(blank=True, null=True, default=0) 
    pieces      =   models.FloatField(blank=True, null=True, default=0) 
    length      =   models.FloatField(blank=True, null=True, default=0) 
    height      =   models.FloatField(blank=True, null=True, default=0) 
    width       =   models.FloatField(blank=True, null=True, default=0) 
    weight      =   models.FloatField(blank=True, null=True, default=0)    
    volume      =   models.FloatField(blank=True, null=True, default=0)