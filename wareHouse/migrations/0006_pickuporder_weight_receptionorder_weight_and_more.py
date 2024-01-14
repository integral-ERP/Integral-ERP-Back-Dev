# Generated by Django 4.2.3 on 2024-01-14 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
        ('wareHouse', '0005_prealert'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickuporder',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='receptionorder',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='releaseorder',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='prealert',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to='maintenance.customer'),
        ),
    ]
