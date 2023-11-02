# Generated by Django 4.2.3 on 2023-11-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paymentTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('dueDays', models.IntegerField(blank=True, null=True)),
                ('discountPercentage', models.IntegerField(blank=True, null=True)),
                ('discountDays', models.IntegerField(blank=True, null=True)),
                ('inactive', models.BooleanField(default=False)),
            ],
        ),
    ]
