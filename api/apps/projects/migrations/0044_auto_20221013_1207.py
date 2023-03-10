# Generated by Django 4.0.2 on 2022-10-13 12:07

from django.db import migrations


def migrate_helicopter_type_tenant(apps, *args):
    HelicopterType = apps.get_model('projects', 'HelicopterType')

    for helicopter_type in HelicopterType.objects.all():
        helicopter_type.tenant = helicopter_type.asset.tenant
        helicopter_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0043_helicoptertype_tenant'),
    ]

    operations = [migrations.RunPython(migrate_helicopter_type_tenant)]
