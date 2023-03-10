# Generated by Django 4.0.2 on 2022-05-04 10:30

import django.db.models.constraints
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_planwellrelation_order'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='planwellrelation',
            constraint=models.UniqueConstraint(
                deferrable=django.db.models.constraints.Deferrable['DEFERRED'],
                fields=('plan', 'order'),
                name='unique_plan_well_relation_order',
            ),
        ),
    ]
