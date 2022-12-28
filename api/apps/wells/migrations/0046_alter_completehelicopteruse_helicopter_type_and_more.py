# Generated by Django 4.0.2 on 2022-10-13 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0021_helicoptertype'),
        ('wells', '0045_rename_helicopter_completehelicopteruse_helicopter_type_and_more'),
        ('projects', '0046_rename_helicoptertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completehelicopteruse',
            name='helicopter_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.helicoptertype'),
        ),
        migrations.AlterField(
            model_name='plannedhelicopteruse',
            name='helicopter_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.helicoptertype'),
        ),
    ]
