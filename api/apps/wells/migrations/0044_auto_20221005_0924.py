# Generated by Django 4.0.2 on 2022-10-05 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0043_alter_wellplannercompletestep_phase_and_more'),
    ]

    database_operations = [migrations.AlterModelTable('wellplannermode', 'emissions_wellplannermode')]

    operations = [migrations.SeparateDatabaseAndState(database_operations=database_operations, state_operations=[])]
