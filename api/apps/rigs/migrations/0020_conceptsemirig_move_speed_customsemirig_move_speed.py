# Generated by Django 4.0.2 on 2022-06-24 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0019_auto_20220623_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='conceptsemirig',
            name='move_speed',
            field=models.FloatField(
                default=6.0,
                help_text='Move speed (kn)',
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customsemirig',
            name='move_speed',
            field=models.FloatField(
                blank=True,
                help_text='Move speed (kn)',
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
        ),
    ]
