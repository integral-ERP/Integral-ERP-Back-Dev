# Generated by Django 4.2.3 on 2023-10-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wareHouse", "0002_alter_releaseorder_client_to_bill"),
    ]

    operations = [
        migrations.AddField(
            model_name="releaseorder",
            name="charges",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
