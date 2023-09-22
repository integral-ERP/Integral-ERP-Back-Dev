from django.db import models

from maintenance.models import employee, forWardingAgents, carrier, customer, vendor, wareHouseProviders

######################### Create your models here. #################################

class pickUpOrder(models.Model):
    status              =   models.CharField(max_length=200, blank=True, null=True)
    number              =   models.PositiveBigIntegerField(blank=True, null=True)
    creationDate        =   models.DateField(blank=True, null=True)
    pickUpDate          =   models.DateField(blank=True, null=True)
    deliveryDate        =   models.DateField(blank=True, null=True)
    date                =   models.DateField(blank=True, null=True)
    issuedByKey         =   models.CharField(max_length=200, blank=True, null=True)
    destinationAgentKey =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.DO_NOTHING) 
    employeekey         =   models.ForeignKey(employee, blank=True, null=True, on_delete=models.DO_NOTHING)     
    shipperkey          =   models.CharField(max_length=200, blank=True, null=True)
    PickUpLocationkey   =   models.TextField(blank=True, null=True)
    consigneekey        =   models.TextField(blank=True, null=True)
    deliveryLocationkey =   models.CharField(max_length=200, blank=True, null=True)
    inlandCarrierKey    =   models.ForeignKey(carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='inlandCarri') 
    mainCarrierKey      =   models.ForeignKey(carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='mainCarri')
    proNumber           =   models.CharField(max_length=200, blank=True, null=True)
    trackingNumber      =   models.CharField(max_length=200, blank=True, null=True)
    supplierKey         =   models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING) 
    invoiceNumber       =   models.CharField(max_length=200, blank=True, null=True)
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

