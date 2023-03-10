# Generated by Django 4.0.2 on 2022-10-10 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0017_remove_vesseltype_asset_alter_vesseltype_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesseltype',
            name='co2_per_fuel',
            field=models.FloatField(
                default=0, help_text='Ton CO2/m3 fuel', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='co2_tax',
            field=models.FloatField(
                default=0, help_text='CO2 tax (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='fuel_cost',
            field=models.FloatField(
                default=0, help_text='Fuel cost (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='fuel_density',
            field=models.FloatField(
                default=0, help_text='Fuel density (kg/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='fuel_type',
            field=models.CharField(default='Fuel type', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='nox_per_fuel',
            field=models.FloatField(
                default=0, help_text='Kg NOx/Ton Fuel', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='nox_tax',
            field=models.FloatField(
                default=0, help_text='NOx tax (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vesseltype',
            name='fuel_summer',
            field=models.FloatField(
                help_text='Fuel consumption summer (m3/day)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='vesseltype',
            name='fuel_winter',
            field=models.FloatField(
                help_text='Fuel consumption winter (m3/day)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
