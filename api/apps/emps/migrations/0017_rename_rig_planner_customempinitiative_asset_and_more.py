# Generated by Django 4.0.2 on 2022-09-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0016_alter_customempinitiative_rig_planner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customempinitiative',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customenergyuse',
            old_name='rig_planner',
            new_name='asset',
        ),
    ]