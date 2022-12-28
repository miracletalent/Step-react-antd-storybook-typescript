# Generated by Django 4.0.2 on 2022-09-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0002_remove_asset_description_asset_design_description_and_more'),
        ('projects', '0033_alter_customcarboncapturestoragesystem_rig_planner_and_more'),
    ]

    state_operations = [
        migrations.DeleteModel(name='RigPlanner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customcarboncapturestoragesystem',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customcement',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customexternalsupply',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customhelicopter',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customsteel',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='customvessel',
            old_name='rig_planner',
            new_name='asset',
        ),
        migrations.AlterUniqueTogether(
            name='customcarboncapturestoragesystem',
            unique_together={('asset', 'carbon_capture_storage_system')},
        ),
        migrations.AlterUniqueTogether(
            name='customcement',
            unique_together={('asset', 'cement')},
        ),
        migrations.AlterUniqueTogether(
            name='customexternalsupply',
            unique_together={('asset', 'external_supply')},
        ),
        migrations.AlterUniqueTogether(
            name='customhelicopter',
            unique_together={('asset', 'helicopter')},
        ),
        migrations.AlterUniqueTogether(
            name='customsteel',
            unique_together={('asset', 'steel')},
        ),
        migrations.AlterUniqueTogether(
            name='customvessel',
            unique_together={('asset', 'vessel')},
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
        ),
    ]