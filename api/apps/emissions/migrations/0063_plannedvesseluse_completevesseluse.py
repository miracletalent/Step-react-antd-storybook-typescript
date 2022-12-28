# Generated by Django 4.0.2 on 2022-12-01 11:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import apps.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0067_remove_plannedvesseluse_vessel_type_and_more'),
        ('emissions', '0062_wellname_wellname_unique_well_name'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='PlannedVesselUse',
                    fields=[
                        (
                            'id',
                            models.BigAutoField(
                                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                            ),
                        ),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                        (
                            'duration',
                            models.FloatField(
                                help_text='Duration (days)', validators=[apps.core.validators.GreaterThanValidator(0)]
                            ),
                        ),
                        (
                            'exposure_against_current_well',
                            models.FloatField(
                                help_text='Percentage exposure against current well',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        (
                            'waiting_on_weather',
                            models.FloatField(
                                help_text='Waiting on weather contingency (%)',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        (
                            'season',
                            models.CharField(choices=[('SUMMER', 'Summer'), ('WINTER', 'Winter')], max_length=16),
                        ),
                        (
                            'quota_obligation',
                            models.FloatField(
                                help_text='Percentage quota obligation',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        (
                            'vessel_type',
                            models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.vesseltype'),
                        ),
                        (
                            'well_planner',
                            models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wells.wellplanner'),
                        ),
                    ],
                    options={
                        'abstract': False,
                    },
                ),
                migrations.CreateModel(
                    name='CompleteVesselUse',
                    fields=[
                        (
                            'id',
                            models.BigAutoField(
                                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                            ),
                        ),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                        (
                            'duration',
                            models.FloatField(
                                help_text='Duration (days)', validators=[apps.core.validators.GreaterThanValidator(0)]
                            ),
                        ),
                        (
                            'exposure_against_current_well',
                            models.FloatField(
                                help_text='Percentage exposure against current well',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        (
                            'waiting_on_weather',
                            models.FloatField(
                                help_text='Waiting on weather contingency (%)',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        (
                            'season',
                            models.CharField(choices=[('SUMMER', 'Summer'), ('WINTER', 'Winter')], max_length=16),
                        ),
                        (
                            'quota_obligation',
                            models.FloatField(
                                help_text='Percentage quota obligation',
                                validators=[django.core.validators.MinValueValidator(0)],
                            ),
                        ),
                        ('approved', models.BooleanField()),
                        (
                            'vessel_type',
                            models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.vesseltype'),
                        ),
                        (
                            'well_planner',
                            models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wells.wellplanner'),
                        ),
                    ],
                    options={
                        'abstract': False,
                    },
                ),
            ]
        )
    ]
