# Generated by Django 4.0.2 on 2022-09-12 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0025_auto_20220912_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='mode_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.wellplannermode'),
        ),
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='phase_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.wellplannerphase'),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='mode_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.wellplannermode'),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='phase_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.wellplannerphase'),
        ),
    ]
