from django.db import models

from maintenance.models import Carrier, Agent, Vendor, Customer, Employee, Port, PackageType, Location, Company,Shipper,PickUpLocation,Consignee,DeliveryLocation,ClientToBill, ReleasedTo

######################### Create your models here. #################################

class PickUpOrder(models.Model):
    status                  =   models.CharField(max_length=200, blank=True, null=True)
    number                  =   models.PositiveBigIntegerField(blank=True, null=True)
    creation_date           =   models.DateField(blank=True, null=True)
    pick_up_date            =   models.DateField(blank=True, null=True)
    delivery_date           =   models.DateField(blank=True, null=True)
    date                    =   models.DateField(blank=True, null=True)
    issued_by               =   models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='issuedBy')
    destination_agent       =   models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING,related_name='pickUpDestinationAgent') 
    employee                =   models.ForeignKey(Employee, blank=True, null=True, on_delete=models.DO_NOTHING,related_name='employee')     
    shipper                 =   models.ForeignKey(Shipper, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpShipper')
    pick_up_location        =   models.ForeignKey(PickUpLocation, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpLocation')
    consignee               =   models.ForeignKey(Consignee, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpConsignee')
    client_to_bill          =   models.ForeignKey(ClientToBill, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpclientToBill')
    delivery_location       =   models.ForeignKey(DeliveryLocation, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='deliveryLocation')
    inland_carrier          =   models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='inlandCarrier') 
    main_carrier            =   models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpCarrier')
    pro_number              =   models.CharField(max_length=200, blank=True, null=True)
    tracking_number         =   models.CharField(max_length=200, blank=True, null=True)
    supplier                =   models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING) 
    invoice_number          =   models.CharField(max_length=200, blank=True, null=True)
    purchase_order_number   =   models.CharField(max_length=200, blank=True, null=True)
    commodities             =   models.JSONField(blank=True, null=True)
    charges                 =   models.JSONField(blank=True, null=True)
    weight = models.IntegerField(default=0, null=True)
    disabled = models.BooleanField(default=False)

class ReceptionOrder(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    number =  models.PositiveBigIntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.DO_NOTHING)
    issued_by = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING)
    destination_agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='receptionDestinationAgent')
    shipper = models.ForeignKey(Shipper, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='receptionShipper')
    consignee = models.ForeignKey(Consignee, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='receptionConsignee')
    client_to_bill = models.ForeignKey(ClientToBill, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='clientToBill')
    main_carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='receptionCarrier')
    supplier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='receptionSupplier')
    commodities  = models.JSONField(blank=True, null=True)
    events = models.JSONField(blank=True, null=True)
    attachments = models.JSONField(blank=True, null=True)
    notes = models.JSONField(blank=True, null=True)
    charges = models.JSONField(blank=True, null=True)
    pro_number              =   models.CharField(max_length=200, blank=True, null=True)
    tracking_number         =   models.CharField(max_length=200, blank=True, null=True)
    invoice_number          =   models.CharField(max_length=200, blank=True, null=True)
    purchase_order_number   =   models.CharField(max_length=200, blank=True, null=True)
    weight = models.IntegerField(default=0, null=True)
    disabled = models.BooleanField(default=False)
    
class ReleaseOrder(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    number =  models.PositiveBigIntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="releaseEmployee")
    issued_by = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="releaseAgent")
    carrier = models.ForeignKey(Carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='releaseCarrier')
    client_to_bill = models.ForeignKey(ClientToBill, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='releaseclientToBill')
    released_to = models.ForeignKey(ReleasedTo, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='releaseReleaseTo')
    warehouse_receipt = models.ForeignKey(PickUpOrder, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="pickupOrder")
    pro_number              =   models.CharField(max_length=200, blank=True, null=True)
    tracking_number         =   models.CharField(max_length=200, blank=True, null=True)
    purchase_order_number   =   models.CharField(max_length=200, blank=True, null=True)
    weight = models.IntegerField(default=0, null=True)
    commodities  = models.JSONField(blank=True, null=True)
    charges = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)

class PreAlert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tracking_number = models.CharField(max_length=200, blank=True, null=True)
    store = models.CharField(max_length=200, blank=True, null=True)
    courier = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey(Customer, related_name="client", on_delete=models.DO_NOTHING)
    packages = models.JSONField(blank=True, null=True)
    disabled = models.BooleanField(default=False)