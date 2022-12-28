# Generated by Django 4.0.2 on 2022-09-28 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0018_alter_customempinitiativephase_unique_together_and_more'),
        ('wells', '0037_alter_wellplannercompletestep_emp_initiatives_and_more'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterUniqueTogether(
                    name='customempinitiativephase',
                    unique_together=None,
                ),
                migrations.RemoveField(
                    model_name='customempinitiativephase',
                    name='emp_initiative',
                ),
                migrations.RemoveField(
                    model_name='customempinitiativephase',
                    name='mode',
                ),
                migrations.RemoveField(
                    model_name='customempinitiativephase',
                    name='phase',
                ),
                migrations.RemoveField(
                    model_name='customenergyuse',
                    name='asset',
                ),
                migrations.AlterUniqueTogether(
                    name='customenergyusephase',
                    unique_together=None,
                ),
                migrations.RemoveField(
                    model_name='customenergyusephase',
                    name='energy_use',
                ),
                migrations.RemoveField(
                    model_name='customenergyusephase',
                    name='mode',
                ),
                migrations.RemoveField(
                    model_name='customenergyusephase',
                    name='phase',
                ),
                migrations.DeleteModel(
                    name='CustomEmpInitiative',
                ),
                migrations.DeleteModel(
                    name='CustomEmpInitiativePhase',
                ),
                migrations.DeleteModel(
                    name='CustomEnergyUse',
                ),
                migrations.DeleteModel(
                    name='CustomEnergyUsePhase',
                ),
            ],
            database_operations=[],
        ),
    ]