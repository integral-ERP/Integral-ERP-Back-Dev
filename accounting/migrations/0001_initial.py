# Generated by Django 4.2.3 on 2024-06-18 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("maintenance", "0001_initial"),
        ("configuration", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChartAccounts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("type", models.CharField(blank=True, max_length=100, null=True)),
                ("referenceNum", models.BigIntegerField(blank=True, null=True)),
                ("balanceUSD", models.BigIntegerField(blank=True, null=True)),
                ("currency", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "parentAccount",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "accountNumber",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("note", models.CharField(blank=True, max_length=100, null=True)),
                ("typeChart", models.CharField(blank=True, max_length=100, null=True)),
                ("disabled", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Deposits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bankAccount",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("date", models.DateField(blank=True, null=True)),
                ("memo", models.CharField(blank=True, max_length=200, null=True)),
                ("depositCharges", models.JSONField(blank=True, null=True)),
                ("total", models.CharField(blank=True, max_length=200, null=True)),
                ("disabled", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ItemServices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("type", models.CharField(blank=True, max_length=100, null=True)),
                ("amount", models.FloatField(blank=True, null=True)),
                (
                    "autCreation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("currency", models.CharField(blank=True, max_length=100, null=True)),
                ("iataCode", models.CharField(blank=True, max_length=100, null=True)),
                ("disabled", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="OpeningBalance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("balance", models.FloatField(blank=True, null=True)),
                ("disabled", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "customerByName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "amountReceived",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                ("trasaDate", models.DateField(blank=True, null=True)),
                ("number", models.CharField(blank=True, max_length=200, null=True)),
                ("memo", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "accountByType",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountRecei",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountByBankType",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountReceiBank",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("disabled", models.BooleanField(default=False)),
                (
                    "accountByBankId",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="accountByBankId",
                        to="accounting.chartaccounts",
                    ),
                ),
                (
                    "accountById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounting.chartaccounts",
                    ),
                ),
                (
                    "customerById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="maintenance.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(blank=True, max_length=200, null=True)),
                ("number", models.CharField(blank=True, max_length=200, null=True)),
                ("account", models.CharField(blank=True, max_length=200, null=True)),
                ("paymentTem", models.CharField(blank=True, max_length=200, null=True)),
                ("division", models.CharField(blank=True, max_length=200, null=True)),
                ("apply", models.CharField(blank=True, max_length=200, null=True)),
                ("due", models.DateField(blank=True, null=True)),
                ("trasaDate", models.DateField(blank=True, null=True)),
                ("bilingAddres", models.TextField(blank=True, null=True)),
                ("currency", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "issuedByName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "invoiceById",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "invoiceBydescription",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "paymentByDesc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountByType",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "accountByName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("typeByCode", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "typeService",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("paidAdd", models.CharField(blank=True, max_length=200, null=True)),
                ("exchangeRate", models.BigIntegerField(blank=True, null=True)),
                ("invoiceCharges", models.JSONField(blank=True, null=True)),
                ("disabled", models.BooleanField(default=False)),
                (
                    "accountById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounting.chartaccounts",
                    ),
                ),
                (
                    "issued_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="maintenance.agent",
                    ),
                ),
                (
                    "paymentById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.paymentterms",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(blank=True, max_length=200, null=True)),
                ("number", models.CharField(blank=True, max_length=200, null=True)),
                ("due", models.DateField(blank=True, null=True)),
                ("trasaDate", models.DateField(blank=True, null=True)),
                (
                    "accountByType",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "carriVerndorByName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "paymentByDesc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("billCharges", models.JSONField(blank=True, null=True)),
                ("disabled", models.BooleanField(default=False)),
                (
                    "accountById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounting.chartaccounts",
                    ),
                ),
                (
                    "carriVerndorById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="maintenance.vendor",
                    ),
                ),
                (
                    "paymentById",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.paymentterms",
                    ),
                ),
            ],
        ),
    ]
