# Generated by Django 4.0.2 on 2022-10-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0030_merge_20221020_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='helicoptertype',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
