# Generated by Django 4.0.2 on 2022-10-24 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0031_externalenergysupply'),
        ('wells', '0049_alter_wellplannercompletestep_external_energy_supply_and_more'),
        ('projects', '0057_delete_externalenergysupply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='external_energy_supply',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='emissions.externalenergysupply'
            ),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='external_energy_supply',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='emissions.externalenergysupply'
            ),
        ),
    ]
