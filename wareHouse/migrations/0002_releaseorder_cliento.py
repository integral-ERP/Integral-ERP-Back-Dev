# Generated by Django 5.0.4 on 2024-08-30 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
        ('wareHouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='releaseorder',
            name='clienTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintenance.customer'),
        ),
    ]
