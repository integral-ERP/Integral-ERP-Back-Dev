# Generated by Django 4.2.3 on 2023-11-28 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('type_person', models.CharField(blank=True, default='agent', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('carrier_type', models.CharField(blank=True, max_length=200, null=True)),
                ('method_code', models.CharField(blank=True, max_length=200, null=True)),
                ('carrier_code', models.CharField(blank=True, max_length=200, null=True)),
                ('scac_number', models.CharField(blank=True, max_length=200, null=True)),
                ('iata_code', models.CharField(blank=True, max_length=200, null=True)),
                ('airline_code', models.CharField(blank=True, max_length=200, null=True)),
                ('airline_prefix', models.CharField(blank=True, max_length=200, null=True)),
                ('airway_bill_number', models.TextField(blank=True, null=True)),
                ('passenger_only_airline', models.BooleanField(default=False)),
                ('type_person', models.CharField(blank=True, default='Carrier', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, default='none', max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('division', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.TextField()),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('port', models.CharField(blank=True, max_length=200, null=True)),
                ('type_logistic_provider', models.BooleanField(default=False)),
                ('type_distribution', models.BooleanField(default=False)),
                ('type_airline_carrier', models.BooleanField(default=False)),
                ('type_ocean_carrier', models.BooleanField(blank=True, default=False, null=True)),
                ('type_company_warehouse', models.BooleanField(blank=True, default=False, null=True)),
                ('company_iata_code', models.CharField(blank=True, max_length=200, null=True)),
                ('company_fmc_code', models.CharField(blank=True, max_length=200, null=True)),
                ('company_scac_code', models.CharField(blank=True, max_length=200, null=True)),
                ('company_tsa_code', models.CharField(blank=True, max_length=200, null=True)),
                ('company_img_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_img_logo', models.ImageField(blank=True, null=True, upload_to='./logo')),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('type_person', models.CharField(blank=True, default='customer', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('type_person', models.CharField(blank=True, default='employee', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('empty', models.BooleanField(blank=True, default=False, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('zone', models.CharField(blank=True, max_length=200, null=True)),
                ('length', models.FloatField(blank=True, max_length=200, null=True)),
                ('width', models.FloatField(blank=True, max_length=200, null=True)),
                ('height', models.FloatField(blank=True, max_length=200, null=True)),
                ('volume', models.FloatField(blank=True, max_length=200, null=True)),
                ('weight', models.FloatField(blank=True, max_length=200, null=True)),
                ('max_weight', models.FloatField(blank=True, max_length=200, null=True)),
                ('disabled', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('length', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('max_weight', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('type_code', models.CharField(blank=True, max_length=200, null=True)),
                ('container_code', models.CharField(blank=True, max_length=200, null=True)),
                ('container_type', models.CharField(blank=True, max_length=200, null=True)),
                ('ground', models.BooleanField(blank=True, default=False, null=True)),
                ('air', models.BooleanField(blank=True, default=False, null=True)),
                ('ocean', models.BooleanField(blank=True, default=False, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('method', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_division', models.CharField(blank=True, max_length=200, null=True)),
                ('used', models.BooleanField(blank=True, default=False, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('air', models.BooleanField(blank=True, default=False, null=True)),
                ('maritime', models.BooleanField(blank=True, default=False, null=True)),
                ('rail', models.BooleanField(blank=True, default=False, null=True)),
                ('road', models.BooleanField(blank=True, default=False, null=True)),
                ('mail', models.BooleanField(blank=True, default=False, null=True)),
                ('border_crossing', models.BooleanField(blank=True, default=False, null=True)),
                ('us_customs_code', models.CharField(blank=True, max_length=200, null=True)),
                ('type_person', models.CharField(blank=True, default='port', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=200, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=200, null=True)),
                ('street_and_number', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('type_person', models.CharField(blank=True, default='vendor', max_length=200, null=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('vendorid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipper_agent', to='maintenance.agent')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipper_customer', to='maintenance.customer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipper_vendor', to='maintenance.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='ReleasedTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('vendorid', models.CharField(blank=True, max_length=200, null=True)),
                ('carrierid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='releasedto_agent', to='maintenance.agent')),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='releasedto_carrier', to='maintenance.carrier')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='releasedto_customer', to='maintenance.customer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='releasedto_vendor', to='maintenance.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PickUpLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('vendorid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pickup_agent', to='maintenance.agent')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pickup_customer', to='maintenance.customer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pickup_vendor', to='maintenance.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('vendorid', models.CharField(blank=True, max_length=200, null=True)),
                ('carrierid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery_agent', to='maintenance.agent')),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery_carrier', to='maintenance.carrier')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery_customer', to='maintenance.customer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery_vendor', to='maintenance.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('vendorid', models.CharField(blank=True, max_length=200, null=True)),
                ('carrierid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consignee_agent', to='maintenance.agent')),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consignee_carrier', to='maintenance.carrier')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consignee_customer', to='maintenance.customer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consignee_vendor', to='maintenance.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='ClientToBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipperid', models.CharField(blank=True, max_length=200, null=True)),
                ('consigneeid', models.CharField(blank=True, max_length=200, null=True)),
                ('customerid', models.CharField(blank=True, max_length=200, null=True)),
                ('agentid', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_agent', to='maintenance.agent')),
                ('consignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_consignee', to='maintenance.consignee')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_customer', to='maintenance.customer')),
                ('shipper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_shipper', to='maintenance.shipper')),
            ],
        ),
    ]
