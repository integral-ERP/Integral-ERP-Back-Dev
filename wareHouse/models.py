from django.db import models

# Create your models here.

class pickUpOrder(models.Model):
    status          =   models.CharField(max_length=200, blank=True, null=True)
    number          =   models.PositiveBigIntegerField(blank=True, null=True)
    date            =   models.DateField(blank=True, null=True)
    shipper         =   models.TextField(blank=True, null=True)
    consignee       =   models.TextField(blank=True, null=True)
    PickUpOrder     =   models.TextField(blank=True, null=True)
    deliveryName    =   models.CharField(max_length=200, blank=True, null=True)
    piedes          =   models.PositiveSmallIntegerField(blank=True, null=True)
    carrier         =   models.CharField(max_length=200, blank=True, null=True)
    weight          =   models.FloatField(blank=True, null=True, default=0)    
    volume          =   models.FloatField(blank=True, null=True, default=0)

    