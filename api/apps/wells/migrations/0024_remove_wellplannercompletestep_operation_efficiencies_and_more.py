# Generated by Django 4.0.2 on 2022-09-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0023_alter_wellplanner_current_step'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='operation_efficiencies',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='operation_efficiencies',
        ),
    ]