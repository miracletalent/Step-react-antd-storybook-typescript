# Generated by Django 4.0.2 on 2022-10-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0048_merge_20221017_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='customexternalsupply',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
