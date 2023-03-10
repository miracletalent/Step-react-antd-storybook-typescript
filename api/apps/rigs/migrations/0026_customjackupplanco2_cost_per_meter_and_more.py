# Generated by Django 4.0.2 on 2022-09-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0025_alter_conceptdrillship_hull_depth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customjackupplanco2',
            name='cost_per_meter',
            field=models.FloatField(default=0, help_text='Cost per meter (USD)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customsemiplanco2',
            name='cost_per_meter',
            field=models.FloatField(default=0, help_text='Cost per meter (USD)'),
            preserve_default=False,
        ),
    ]
