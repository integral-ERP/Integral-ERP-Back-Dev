# Generated by Django 4.2.3 on 2023-09-25 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_remove_shipper_agent_remove_shipper_customer_and_more'),
        ('wareHouse', '0004_alter_pickuporder_shipper'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shipper',
        ),
    ]
