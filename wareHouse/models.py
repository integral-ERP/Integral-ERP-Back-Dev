from django.db import models

from maintenance.models import Carrier, Agent, Vendor, Customer, Employee, Port, PackageType, Location, Company

######################### Create your models here. #################################

class Shipper(models.Model):
    customer    = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    agent       = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING)
    vendor      = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.DO_NOTHING)

class PickUpOrder(models.Model):
    status                  =   models.CharField(max_length=200, blank=True, null=True)
    number                  =   models.PositiveBigIntegerField(blank=True, null=True)
    creation_date           =   models.DateField(blank=True, null=True)
    pick_up_date            =   models.DateField(blank=True, null=True)
    delivery_date           =   models.DateField(blank=True, null=True)
    date                    =   models.DateField(blank=True, null=True)
    issued_by               =   models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='issuedBy')
    destination_agent       =   models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING) 
    employee                =   models.ForeignKey(Employee, blank=True, null=True, on_delete=models.DO_NOTHING)     
    shipper                 =   models.ForeignKey(Shipper, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='shipper')
    pick_up_location        =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpLocation')
    consignee               =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='consigneekey')
    delivery_location       =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='deliveryLocation')
    inland_carrier          =   models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='inlandCarri') 
    main_carrier            =   models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='mainCarri')
    pro_number              =   models.CharField(max_length=200, blank=True, null=True)
    tracking_number         =   models.CharField(max_length=200, blank=True, null=True)
    supplier                =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING) 
    invoice_number          =   models.CharField(max_length=200, blank=True, null=True)
    purchase_order_number   =   models.CharField(max_length=200, blank=True, null=True)
  
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
