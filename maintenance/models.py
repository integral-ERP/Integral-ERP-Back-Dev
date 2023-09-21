from django.db import models

# Create your models here.

class carrier(models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    movelPhone      =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification   =   models.CharField(max_length=200, blank=True, null=True)
    typeIdentificacion  =   models.CharField(max_length=200, blank=True, null=True)
    sistenID        =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    parentAccount   =   models.CharField(max_length=200, blank=True, null=True)
    carrierType     =   models.CharField(max_length=200, blank=True, null=True)
    methodCode      =   models.CharField(max_length=200, blank=True, null=True)
    carrierCode     =   models.CharField(max_length=200, blank=True, null=True)
    scacNumber      =   models.CharField(max_length=200, blank=True, null=True)
    iataCode        =   models.CharField(max_length=200, blank=True, null=True)
    airlineCode     =   models.CharField(max_length=200, blank=True, null=True)
    airlinePrefix   =   models.CharField(max_length=200, blank=True, null=True)
    airwayBillNumbers    =  models.TextField(blank=True, null=True)
    passengerOnlyAirline =  models.BooleanField(default=False)
    TypePerson      =   models.CharField(max_length=200, blank=True, null=True, default="Carrier")

    def __str__(self):
        return self.name

class port(models.Model):
    code            =   models.CharField(max_length=200, blank=True, null=True)
    name            =   models.CharField(max_length=200, blank=True, null=True)
    method          =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    subdivision     =   models.CharField(max_length=200, blank=True, null=True)
    used            =   models.BooleanField(default=False)
    remarks         =   models.CharField(max_length=200, blank=True, null=True)
    air             =   models.BooleanField(default=False)
    maritime        =   models.BooleanField(default=False)
    rail            =   models.BooleanField(default=False)
    road            =   models.BooleanField(default=False)
    mail            =   models.BooleanField(default=False)
    borderCrossing  =   models.BooleanField(default=False)
    usCustomsCode   =   models.CharField(max_length=200, blank=True, null=True)
    TypePerson      =   models.CharField(max_length=200, blank=True, null=True, default="Port")

    def __str__(self):
        return self.name

class vendor(models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    movelPhone      =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification = models.CharField(max_length=200, blank=True, null=True)
    typeIdentificacion = models.CharField(max_length=200, blank=True, null=True)
    sistenID        =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    TypePerson      =   models.CharField(max_length=200, blank=True, null=True, default="Vendor")

    def __str__(self):
        return self.name

class employee(models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    movelPhone      =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification = models.CharField(max_length=200, blank=True, null=True)
    typeIdentificacion = models.CharField(max_length=200, blank=True, null=True)
    sistenID        =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    TypePerson      =   models.CharField(max_length=200, blank=True, null=True, default="Employee")

    def __str__(self):
        return self.name
    
class company(models.Model):
    nameCompany     =   models.CharField(max_length=200, blank=True, null=True)
    idEntity        =   models.CharField(max_length=50, blank=True, null=True)
    telephon        =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    numCuent        =   models.IntegerField(blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification = models.CharField(max_length=200, blank=True, null=True)
    division        =   models.CharField(max_length=200, blank=True, null=True)
    idNetWord       =   models.IntegerField(blank=True, null=True)

class address(models.Model):
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.IntegerField(blank=True, null=True)
    port            =   models.IntegerField(blank=True, null=True)

class companyType(models.Model):
    logisticsProvi  =   models.BooleanField(default=False)
    distribution    =   models.BooleanField(default=False)
    airlineCarrier  =   models.BooleanField(default=False)
    oceanCarrier    =   models.BooleanField(default=False)
    companyWarehouse =  models.BooleanField(default=False)

class companyInfo(models.Model):
    nameCompany     =   models.CharField(max_length=200, blank=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True)
    webSide         =   models.CharField(max_length=200, blank=True)
    firstNameContac =   models.CharField(max_length=200, blank=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True)

class addressInfo(models.Model):
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True)
    country         =   models.CharField(max_length=200, blank=True)
    state           =   models.CharField(max_length=200, blank=True)
    zipCode         =   models.IntegerField(blank=True, null=True)

class companyRegisCode(models.Model):
    iataCode        =   models.CharField(max_length=200, blank=True)
    fmc             =   models.CharField(max_length=200, blank=True)
    scacCodeUs      =   models.CharField(max_length=200, blank=True)
    tsaNumber       =   models.CharField(max_length=200, blank=True)

class companyLogo(models.Model):
    imgName         =   models.CharField(max_length=200, blank=True)
    imgLogo         =   models.ImageField(upload_to='./logo', blank=True, null=True)

class systCurren(models.Model):
    localCurrency   =   models.CharField(max_length=200, blank=True)
    companyMoreCurren = models.BooleanField(default=False)

class importSchedule(models.Model):
    schedulesB      =   models.BooleanField(default=False)
    schedulesD      =   models.BooleanField(default=False)
    schedulesK      =   models.BooleanField(default=False)

class packType(models.Model):
    description     =   models.CharField(max_length=200, blank=True, null=True)
    length          =   models.FloatField(blank=True, null=True, default=0)
    height          =   models.FloatField(blank=True, null=True, default=0)
    width           =   models.FloatField(blank=True, null=True, default=0)
    weight          =   models.FloatField(blank=True, null=True, default=0)
    volume          =   models.FloatField(blank=True, null=True, default=0)
    maxWeight       =   models.FloatField(blank=True, null=True, default=0)
    type            =   models.CharField(max_length=200, blank=True, null=True)
    typeCode        =   models.CharField(max_length=50, blank=True, null=True)
    containerCode   =   models.CharField(max_length=200, blank=True, null=True)
    containerType   =   models.CharField(max_length=200, blank=True, null=True)
    ground          =   models.BooleanField(default=False)
    air             =   models.BooleanField(default=False)
    ocean           =   models.BooleanField(default=False)

    def __str__(self):
        return self.description

class wareHouseProviders (models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    mobilePhone     =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    
class forWardingAgents (models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    movelPhone      =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification = models.CharField(max_length=200, blank=True, null=True)
    typeIdentificacion = models.CharField(max_length=200, blank=True, null=True)
    sistenID        =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    TypePerson      =   models.CharField(max_length=200, blank=True, null=True, default="Agent")

    def __str__(self):
        return self.name
    
class containerType(models.Model):
    type            =   models.CharField(max_length=200, blank=True, null=True)
    description     =   models.CharField(max_length=200, blank=True, null=True)
    containerCode   =   models.CharField(max_length=200, blank=True, null=True)
    containerType   =   models.CharField(max_length=200, blank=True, null=True)
    ground          =   models.BooleanField(default=False)
    air             =   models.BooleanField(default=False)
    ocean           =   models.BooleanField(default=False)

class customer(models.Model):
    name            =   models.CharField(max_length=200, blank=True, null=True)
    phone           =   models.CharField(max_length=200, blank=True, null=True)
    mobilePhone     =   models.CharField(max_length=200, blank=True, null=True)
    email           =   models.CharField(max_length=200, blank=True, null=True)
    fax             =   models.CharField(max_length=200, blank=True, null=True)
    webSide         =   models.CharField(max_length=200, blank=True, null=True)
    referentNumber  =   models.CharField(max_length=200, blank=True, null=True)
    firstNameContac =   models.CharField(max_length=200, blank=True, null=True)
    lasNameContac   =   models.CharField(max_length=200, blank=True, null=True)
    numIdentification   =   models.CharField(max_length=200, blank=True, null=True)
    typeIdentificacion  =   models.CharField(max_length=200, blank=True, null=True)
    sistenID        =   models.CharField(max_length=200, blank=True, null=True)
    streetNumber    =   models.TextField(blank=True, null=True)
    city            =   models.CharField(max_length=200, blank=True, null=True)
    state           =   models.CharField(max_length=200, blank=True, null=True)
    country         =   models.CharField(max_length=200, blank=True, null=True)
    zipCode         =   models.CharField(max_length=200, blank=True, null=True)
    TypePerson      =   models.CharField(max_length=200, blank=True, default='Customer')

    def __str__(self):
        return self.name

class location(models.Model):
    status          =   models.CharField(max_length=200, blank=True, null=True)
    code            =   models.CharField(max_length=200, blank=True, null=True)
    description     =   models.CharField(max_length=200, blank=True, null=True)
    empty           =   models.BooleanField(default=False)
    type            =   models.CharField(max_length=200, blank=True, null=True)
    zone            =   models.CharField(max_length=200, blank=True, null=True)
    length          =   models.FloatField(blank=True, null=True, default=0)
    width           =   models.FloatField(blank=True, null=True, default=0)
    height          =   models.FloatField(blank=True, null=True, default=0)   
    volume          =   models.FloatField(blank=True, null=True, default=0)
    weight          =   models.FloatField(blank=True, null=True, default=0)
    maxWeight       =   models.FloatField(blank=True, null=True, default=0)
    disable         =   models.BooleanField(default=False)

    def __str__(self):
        return self.code

class containerCode(models.Model):
    code            =   models.CharField(max_length=200, blank=True, null=True)
    description     =   models.CharField(max_length=200, blank=True, null=True)

class containerEquipType(models.Model):
    code            =   models.CharField(max_length=200, blank=True, null=True)
    description     =   models.CharField(max_length=200, blank=True, null=True)

class consignee (models.Model):
    customerId      =   models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    vendorId        =   models.ForeignKey(vendor, blank=True, null=True, on_delete=models.DO_NOTHING,related_name='consigneeVendor')
    forwarAgentId   =   models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.DO_NOTHING)
