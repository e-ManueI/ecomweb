# Generated by Django 4.0.4 on 2022-04-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_drive'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fuel',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')], default='Petrol', max_length=6, verbose_name='Fuel Type'),
        ),
        migrations.AddField(
            model_name='product',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Continously variable transmission(CVT)', 'Continously variable transmission(CVT)'), ('Semi-Automatic', 'Semi-Automatic'), ('Dual-clutch', 'Dual-clutch')], default='Automatic', max_length=38, verbose_name='Transmission Type'),
        ),
    ]