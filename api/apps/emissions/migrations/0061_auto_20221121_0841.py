# Generated by Django 4.0.2 on 2022-11-21 08:41

from django.db import migrations
from django.utils import timezone


class AssetSeason:
    SUMMER = 'SUMMER'
    WINTER = 'WINTER'


def add_transport_section(apps, *args):
    ConceptPhase = apps.get_model('emissions', 'ConceptPhase')
    CustomPhase = apps.get_model('emissions', 'CustomPhase')
    Asset = apps.get_model('emissions', 'Asset')
    Tenant = apps.get_model('tenants', 'Tenant')
    CustomMode = apps.get_model('emissions', 'CustomMode')
    Baseline = apps.get_model('emissions', 'Baseline')
    EmissionReductionInitiative = apps.get_model('emissions', 'EmissionReductionInitiative')
    BaselineInput = apps.get_model('emissions', 'BaselineInput')
    EmissionReductionInitiativeInput = apps.get_model('emissions', 'EmissionReductionInitiativeInput')

    for tenant in Tenant.objects.all():
        concept_transport_section = ConceptPhase.objects.create(
            name='Transport section', description='Transport section phase', tenant=tenant, transit=False
        )
        for asset in Asset.objects.filter(tenant=tenant):
            CustomPhase.objects.filter(asset=asset, name=concept_transport_section.name).update(
                name=f'{concept_transport_section.name} {timezone.now().isoformat()}'[:32]
            )
            custom_transport_section = CustomPhase.objects.create(
                phase=concept_transport_section,
                asset=asset,
                name=concept_transport_section.name,
                description=concept_transport_section.description,
            )
            modes = CustomMode.objects.filter(asset=asset).exclude(mode__transit=True)
            for baseline in Baseline.objects.filter(asset=asset):
                for mode in modes:
                    for season in [AssetSeason.SUMMER, AssetSeason.WINTER]:
                        last_input = BaselineInput.objects.filter(baseline=baseline).order_by('order').last()
                        BaselineInput.objects.get_or_create(
                            baseline=baseline,
                            phase=custom_transport_section,
                            mode=mode,
                            season=season,
                            defaults=dict(value=0, order=last_input.order + 1 if last_input else 0),
                        )
                for emission_reduction_initiative in EmissionReductionInitiative.objects.filter(
                    emission_management_plan__baseline=baseline
                ):
                    for mode in modes:
                        EmissionReductionInitiativeInput.objects.get_or_create(
                            emission_reduction_initiative=emission_reduction_initiative,
                            phase=custom_transport_section,
                            mode=mode,
                            defaults=dict(value=0),
                        )


class Migration(migrations.Migration):

    dependencies = [('emissions', '0060_alter_baselineinput_value_and_more'), ('tenants', '0008_auto_20220324_1446')]

    operations = [migrations.RunPython(add_transport_section)]
