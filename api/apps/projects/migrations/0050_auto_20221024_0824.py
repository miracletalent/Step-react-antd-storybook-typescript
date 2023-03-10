# Generated by Django 4.0.2 on 2022-10-24 08:24

from django.db import migrations


def migrate_custom_external_supply_name(apps, *args):
    CustomExternalSupply = apps.get_model("projects", "CustomExternalSupply")

    for custom_external_supply in CustomExternalSupply.objects.all():
        custom_external_supply.name = custom_external_supply.external_supply.name
        custom_external_supply.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_customexternalsupply_name'),
    ]

    operations = [migrations.RunPython(migrate_custom_external_supply_name)]
