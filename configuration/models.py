from django.db import models

# Create your models here.

class paymentTerms(models.Model):
    description         =   models.CharField(max_length=200, blank=True, null=True)
    dueDays             =   models.IntegerField(blank=True, null=True)
    discountPercentage  =   models.IntegerField(blank=True, null=True)
    discountDays        =   models.IntegerField(blank=True, null=True)
    inactive            =   models.BooleanField(default=False)