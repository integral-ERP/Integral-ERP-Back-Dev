from django.db import models

from maintenance.models import employee, forWardingAgents, carrier, customer, vendor, wareHouseProviders

######################### Create your models here. #################################

class shipper(models.Model):
    customerName    =   models.ForeignKey(customer, blank=True, null=True, on_delete=models.CASCADE, related_name='shippers')
    vendorName      =   models.ForeignKey(vendor, blank=True, null=True, on_delete=models.CASCADE, related_name='shippers')
    agentName       =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.CASCADE, related_name='shippers')

class issuedBy(models.Model):
    forWardingAgents    =   models.ForeignKey(forWardingAgents, blank=True, on_delete=models.DO_NOTHING)
    wareHouseProvider   =   models.ForeignKey(wareHouseProviders, blank=True, on_delete=models.DO_NOTHING)

class pickUpLocation(models.Model):
    customerName    =   models.ForeignKey(customer, blank=True, null=True, on_delete=models.CASCADE, related_name='shippersa')
    vendorName      =   models.ForeignKey(vendor, blank=True, null=True, on_delete=models.CASCADE, related_name='shippersb')
    agentName       =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.CASCADE, related_name='shippersc')

class consignee(models.Model):
    customerName    = models.ForeignKey(customer, blank=True, null=True, on_delete=models.CASCADE, related_name='shipp')
    vendorName      =   models.ForeignKey(vendor, blank=True, null=True, on_delete=models.CASCADE, related_name='shi')
    agentName       =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.CASCADE, related_name='sh')
    carrierName     =   models.ForeignKey(carrier, blank=True, null=True, on_delete=models.CASCADE, related_name='sss')

class deliveryLocation(models.Model):
    customerName    = models.ForeignKey(customer, blank=True, null=True, on_delete=models.CASCADE, related_name='ship')
    vendorName      =   models.ForeignKey(vendor, blank=True, null=True, on_delete=models.CASCADE, related_name='ship')
    agentName       =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.CASCADE, related_name='ship')
    carrierName     =   models.ForeignKey(carrier, blank=True, null=True, on_delete=models.CASCADE, related_name='ship')

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

