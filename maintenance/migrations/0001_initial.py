# Generated by Django 4.2.3 on 2023-08-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.IntegerField(blank=True, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='addressInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('zipCode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iataCode', models.CharField(blank=True, max_length=200, null=True)),
                ('fmc', models.CharField(blank=True, max_length=200, null=True)),
                ('scacCodeUs', models.CharField(blank=True, max_length=200, null=True)),
                ('tsaNumber', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('movelPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
                ('parentAccount', models.CharField(blank=True, max_length=200, null=True)),
                ('carrierType', models.CharField(blank=True, max_length=200, null=True)),
                ('methodCode', models.CharField(blank=True, max_length=200, null=True)),
                ('carrierCode', models.CharField(blank=True, max_length=200, null=True)),
                ('scacNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('iataCode', models.CharField(blank=True, max_length=200, null=True)),
                ('airlineCode', models.CharField(blank=True, max_length=200, null=True)),
                ('airlinePrefix', models.CharField(blank=True, max_length=200, null=True)),
                ('airwayBillNumbers', models.TextField(blank=True, null=True)),
                ('passengerOnlyAirline', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCompany', models.CharField(blank=True, max_length=200, null=True)),
                ('idEntity', models.CharField(blank=True, max_length=50, null=True)),
                ('telephon', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('numCuent', models.IntegerField(blank=True, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('division', models.CharField(blank=True, max_length=200, null=True)),
                ('idNetWord', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='companyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCompany', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('webSide', models.CharField(blank=True, max_length=200)),
                ('firstNameContac', models.CharField(blank=True, max_length=200)),
                ('lasNameContac', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='companyLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgName', models.CharField(blank=True, max_length=200)),
                ('imgLogo', models.ImageField(blank=True, null=True, upload_to='./logo')),
            ],
        ),
        migrations.CreateModel(
            name='companyRegisCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iataCode', models.CharField(blank=True, max_length=200)),
                ('fmc', models.CharField(blank=True, max_length=200)),
                ('scacCodeUs', models.CharField(blank=True, max_length=200)),
                ('tsaNumber', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='companyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logisticsProvi', models.BooleanField(default=False)),
                ('distribution', models.BooleanField(default=False)),
                ('airlineCarrier', models.BooleanField(default=False)),
                ('oceanCarrier', models.BooleanField(default=False)),
                ('companyWarehouse', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='containerCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='containerEquipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='containerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('containerCode', models.CharField(blank=True, max_length=200, null=True)),
                ('containerType', models.CharField(blank=True, max_length=200, null=True)),
                ('ground', models.BooleanField(default=False)),
                ('air', models.BooleanField(default=False)),
                ('ocean', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobilePhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('movelPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='forwarAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('movelPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='forWardingAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('movelPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='importSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedulesB', models.BooleanField(default=False)),
                ('schedulesD', models.BooleanField(default=False)),
                ('schedulesK', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('empty', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('zone', models.CharField(blank=True, max_length=200, null=True)),
                ('length', models.FloatField(blank=True, default=0, null=True)),
                ('width', models.FloatField(blank=True, default=0, null=True)),
                ('height', models.FloatField(blank=True, default=0, null=True)),
                ('volume', models.FloatField(blank=True, default=0, null=True)),
                ('weight', models.FloatField(blank=True, default=0, null=True)),
                ('maxWeight', models.FloatField(blank=True, default=0, null=True)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='packType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('length', models.FloatField(blank=True, default=0, null=True)),
                ('height', models.FloatField(blank=True, default=0, null=True)),
                ('width', models.FloatField(blank=True, default=0, null=True)),
                ('weight', models.FloatField(blank=True, default=0, null=True)),
                ('volume', models.FloatField(blank=True, default=0, null=True)),
                ('maxWeight', models.FloatField(blank=True, default=0, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('typeCode', models.CharField(blank=True, max_length=50, null=True)),
                ('containerCode', models.CharField(blank=True, max_length=200, null=True)),
                ('containerType', models.CharField(blank=True, max_length=200, null=True)),
                ('ground', models.BooleanField(default=False)),
                ('air', models.BooleanField(default=False)),
                ('ocean', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('method', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('subdivision', models.CharField(blank=True, max_length=200, null=True)),
                ('used', models.BooleanField(default=False)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('air', models.BooleanField(default=False)),
                ('maritime', models.BooleanField(default=False)),
                ('rail', models.BooleanField(default=False)),
                ('road', models.BooleanField(default=False)),
                ('mail', models.BooleanField(default=False)),
                ('borderCrossing', models.BooleanField(default=False)),
                ('usCustomsCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='systCurren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localCurrency', models.CharField(blank=True, max_length=200)),
                ('companyMoreCurren', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('movelPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('numIdentification', models.CharField(blank=True, max_length=200, null=True)),
                ('typeIdentificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('sistenID', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='wareHouseProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobilePhone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('webSide', models.CharField(blank=True, max_length=200, null=True)),
                ('referentNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('lasNameContac', models.CharField(blank=True, max_length=200, null=True)),
                ('streetNumber', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
