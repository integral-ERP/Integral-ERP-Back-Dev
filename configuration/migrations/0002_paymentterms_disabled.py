# Generated by Django 5.0 on 2024-01-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentterms',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
