# Generated by Django 4.1 on 2024-04-10 23:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_dt', models.DateTimeField(editable=False)),
                ('transaction_id', models.CharField(editable=False, max_length=50, unique=True)),
                ('total_sale', models.DecimalField(decimal_places=2, editable=False, max_digits=7)),
                ('sub_total', models.DecimalField(decimal_places=2, editable=False, max_digits=7)),
                ('tax_total', models.DecimalField(decimal_places=2, editable=False, max_digits=7, null=True)),
                ('deposit_total', models.DecimalField(decimal_places=2, editable=False, max_digits=7, null=True)),
                ('payment_type', models.CharField(choices=[('CASH', 'CASH'), ('DEBIT/CREDIT', 'DEBIT/CREDIT'), ('EBT', 'EBT')], editable=False, max_length=32)),
                ('receipt', models.TextField(editable=False)),
                ('products', models.TextField(editable=False)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='productTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id_num', models.CharField(editable=False, max_length=50)),
                ('transaction_date_time', models.DateTimeField(editable=False)),
                ('barcode', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(editable=False, max_length=125)),
                ('department', models.CharField(editable=False, max_length=125, null=True)),
                ('sales_price', models.DecimalField(decimal_places=2, editable=False, max_digits=7)),
                ('qty', models.IntegerField(default=0, editable=False, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=7, null=True)),
                ('tax_category', models.CharField(editable=False, max_length=125)),
                ('tax_percentage', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=7, null=True)),
                ('deposit_category', models.CharField(editable=False, max_length=125)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('deposit_amount', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=7, null=True)),
                ('payment_type', models.CharField(editable=False, max_length=32)),
                ('transaction', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='transaction.transaction')),
            ],
            options={
                'verbose_name_plural': 'Product Transactions',
            },
        ),
    ]