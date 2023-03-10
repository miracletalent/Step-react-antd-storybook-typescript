# Generated by Django 4.0.2 on 2022-06-09 10:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0014_conceptdrillship_day_rate_and_more'),
        ('projects', '0014_remove_project_drillships_remove_project_jackup_rigs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='operation_end_date',
            new_name='reference_operation_end_date',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='operation_start_date',
            new_name='reference_operation_start_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='psv_avg_fuel_consumption',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tugs_no_used',
        ),
        migrations.AddField(
            model_name='plan',
            name='distance_from_tug_base_to_previous_well',
            field=models.FloatField(default=100, verbose_name='Distance from Tug base to previous well (nm)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='reference_operation_drillship',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rigs.customdrillship'
            ),
        ),
        migrations.AddField(
            model_name='plan',
            name='reference_operation_jackup',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rigs.customjackuprig'
            ),
        ),
        migrations.AddField(
            model_name='plan',
            name='reference_operation_semi',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rigs.customsemirig'
            ),
        ),
        migrations.AddField(
            model_name='planwellrelation',
            name='distance_to_tug_base',
            field=models.FloatField(
                default=100,
                help_text='Distance to Tug base (nm)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planwellrelation',
            name='jackup_positioning_time',
            field=models.FloatField(
                default=1.5,
                help_text='Jackup positioning time (d)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planwellrelation',
            name='semi_positioning_time',
            field=models.FloatField(
                default=1.5,
                help_text='Semi positioning time (d)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='helicopter_cruise_speed',
            field=models.FloatField(
                default=120, help_text='Cruise speed (kn)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='psv_avg_fuel_dp_consumption',
            field=models.FloatField(
                default=5.5,
                help_text='Average PSV fuel DP consumption (t/d)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='psv_avg_fuel_transit_consumption',
            field=models.FloatField(
                default=12,
                help_text='Average PSV fuel transit consumption (t/d)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='psv_loading_time',
            field=models.FloatField(
                default=0.25, help_text='PSV loading time (d)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='psv_speed',
            field=models.FloatField(
                default=12, help_text='PSV speed (kn)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tugs_avg_fuel_consumption',
            field=models.FloatField(
                default=22,
                help_text='Average Tug fuel consumption (t/d)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tugs_move_speed',
            field=models.FloatField(
                default=2.5, help_text='Tug move speed (kn)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tugs_transit_speed',
            field=models.FloatField(
                default=12, help_text='Tug transit speed (kn)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_from_previous_location',
            field=models.FloatField(
                help_text='Distance from previous well (nm)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_ahv_base',
            field=models.FloatField(
                help_text='Distance to AHV base (nm)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_helicopter_base',
            field=models.FloatField(
                help_text='Distance to Helicopter base (nm)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_psv_base',
            field=models.FloatField(
                help_text='Distance to PSV base (nm)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
