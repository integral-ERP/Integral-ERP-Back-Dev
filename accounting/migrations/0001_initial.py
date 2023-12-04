# Generated by Django 4.2.3 on 2023-11-28 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance', '__first__'),
        ('configuration', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('referenceNum', models.BigIntegerField(blank=True, null=True)),
                ('balanceUSD', models.BigIntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('parentAccount', models.CharField(blank=True, max_length=100, null=True)),
                ('accountNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('typeChart', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('accountName', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('autCreation', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('iataCode', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=200, null=True)),
                ('account', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentTem', models.CharField(blank=True, max_length=200, null=True)),
                ('division', models.CharField(blank=True, max_length=200, null=True)),
                ('applyId', models.CharField(blank=True, max_length=200, null=True)),
                ('apply', models.CharField(blank=True, max_length=200, null=True)),
                ('due', models.DateField(blank=True, null=True)),
                ('trasaDate', models.DateField(blank=True, null=True)),
                ('bilingAddres', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=200, null=True)),
                ('issuedByName', models.CharField(blank=True, max_length=200, null=True)),
                ('invoiceById', models.CharField(blank=True, max_length=200, null=True)),
                ('invoiceBydescription', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentByDesc', models.CharField(blank=True, max_length=200, null=True)),
                ('accountByType', models.CharField(blank=True, max_length=200, null=True)),
                ('accountByName', models.CharField(blank=True, max_length=200, null=True)),
                ('typeByCode', models.CharField(blank=True, max_length=200, null=True)),
                ('accounten', models.CharField(blank=True, max_length=200, null=True)),
                ('typeService', models.CharField(blank=True, max_length=200, null=True)),
                ('paidAdd', models.CharField(blank=True, max_length=200, null=True)),
                ('exchangeRate', models.BigIntegerField(blank=True, null=True)),
                ('amount', models.BigIntegerField(blank=True, null=True)),
                ('totalAmount', models.BigIntegerField(blank=True, null=True)),
                ('invoiceCharges', models.JSONField(blank=True, null=True)),
                ('taxCode', models.BigIntegerField(blank=True, null=True)),
                ('amountDue', models.BigIntegerField(blank=True, null=True)),
                ('charges', models.JSONField(blank=True, null=True)),
                ('typeChart', models.CharField(blank=True, max_length=100, null=True)),
                ('accountById', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounting.chartaccounts')),
                ('issued_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintenance.agent')),
                ('paymentById', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configuration.paymentterms')),
            ],
        ),
    ]
