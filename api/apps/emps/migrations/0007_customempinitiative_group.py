# Generated by Django 4.0.2 on 2022-08-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0006_customoperationefficiency_rig_planner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customempinitiative',
            name='group',
            field=models.CharField(
                choices=[
                    ('POWER_SYSTEMS', 'Power systems'),
                    ('BASELOADS', 'Baseloads'),
                    ('PRODUCTIVITY', 'Productivity'),
                ],
                default='POWER_SYSTEMS',
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
