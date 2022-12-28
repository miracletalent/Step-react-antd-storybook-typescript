# Generated by Django 4.0.2 on 2022-06-24 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0020_customsemiplanco2_and_more'),
        ('studies', '0009_alter_studyelement_semi_rigs'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyelementsemirigrelation',
            name='rig_plan_co2',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='rigs.customsemiplanco2'
            ),
        ),
    ]
