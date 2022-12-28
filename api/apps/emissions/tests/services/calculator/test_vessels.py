import pytest
from django.db.models import QuerySet

from apps.emissions.factories import PlannedVesselUseFactory
from apps.emissions.models import PlannedVesselUse
from apps.emissions.services.calculator.vessels import (
    calculate_step_vessels_co2,
    calculate_step_vessels_fuel,
    calculate_vessel_co2,
    calculate_vessel_fuel,
)

# v19.12.22
VESSELS = {
    "Anchor Handling Tug Supply (AHTS)": dict(
        # 'Asset & Material Inputs'!E71
        fuel_consumption=12.0,
        # 'Well Planning'!H19
        waiting_on_weather=5,
        # 'Well Planning'!F19
        duration=7.0,
        # 'Well Planning'!G19
        exposure=20,
        # 'Asset & Material Inputs'!G71
        co2_per_fuel=3.17,
    ),
    "Platform supply vessel (PSV)": dict(
        # 'Asset & Material Inputs'!E72
        fuel_consumption=11.0,
        # 'Well Planning'!H20
        waiting_on_weather=5,
        # 'Well Planning'!F20
        duration=5.0,
        # 'Well Planning'!G20
        exposure=70,
        # 'Asset & Material Inputs'!G72
        co2_per_fuel=3.17,
    ),
    "Stand by vessel (STBY)": dict(
        # 'Asset & Material Inputs'!E73
        fuel_consumption=11.0,
        # 'Well Planning'!H21
        waiting_on_weather=5,
        # 'Well Planning'!F21
        duration=18.0,
        # 'Well Planning'!G21
        exposure=90,
        # 'Asset & Material Inputs'!G73
        co2_per_fuel=3.17,
    ),
    "Multi purpose supply vessels (MPSV)": dict(
        # 'Asset & Material Inputs'!E74
        fuel_consumption=10.0,
        # 'Well Planning'!H22
        waiting_on_weather=5,
        # 'Well Planning'!F22
        duration=7.0,
        # 'Well Planning'!G22
        exposure=100,
        # 'Asset & Material Inputs'!G74
        co2_per_fuel=3.17,
    ),
    "Emergency response and rescue vessels (ERRV)": dict(
        # 'Asset & Material Inputs'!E75
        fuel_consumption=9.0,
        # 'Well Planning'!H23
        waiting_on_weather=5,
        # 'Well Planning'!F23
        duration=3.0,
        # 'Well Planning'!G23
        exposure=10,
        # 'Asset & Material Inputs'!G75
        co2_per_fuel=3.17,
    ),
}


@pytest.fixture
def vessel_uses() -> QuerySet[PlannedVesselUse]:
    for vessel in VESSELS.values():
        PlannedVesselUseFactory(
            waiting_on_weather=vessel["waiting_on_weather"],
            duration=vessel["duration"],
            exposure_against_current_well=vessel["exposure"],
            vessel_type__fuel_consumption_summer=vessel["fuel_consumption"],
            vessel_type__co2_per_fuel=vessel["co2_per_fuel"],
        )

    return PlannedVesselUse.objects.all()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "vessel, expected",
    # v19.12.22
    (
        # 'Calculations'!H59
        ("Anchor Handling Tug Supply (AHTS)", 17.64),
        # 'Calculations'!H60
        ("Platform supply vessel (PSV)", 40.425),
        # 'Calculations'!H61
        ("Stand by vessel (STBY)", 187.11),
        # 'Calculations'!H62
        ("Multi purpose supply vessels (MPSV)", 73.50),
        # 'Calculations'!H63
        ("Emergency response and rescue vessels (ERRV)", 2.8350000000000004),
    ),
)
def test_calculate_vessel_fuel(
    vessel: str,
    expected: float,
):
    assert (
        calculate_vessel_fuel(
            fuel_consumption=VESSELS[vessel]["fuel_consumption"],
            waiting_on_weather=VESSELS[vessel]["waiting_on_weather"],
            duration=VESSELS[vessel]["duration"],
            exposure=VESSELS[vessel]["exposure"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "vessel, expected",
    # v19.12.22
    (
        # 'Calculations'!J59
        ("Anchor Handling Tug Supply (AHTS)", 55.9188),
        # 'Calculations'!J60
        ("Platform supply vessel (PSV)", 128.14724999999999),
        # 'Calculations'!J61
        ("Stand by vessel (STBY)", 593.1387000000001),
        # 'Calculations'!J62
        ("Multi purpose supply vessels (MPSV)", 232.995),
        # 'Calculations'!J63
        ("Emergency response and rescue vessels (ERRV)", 8.98695),
    ),
)
def test_calculate_vessel_co2(
    vessel: str,
    expected: float,
):
    assert (
        calculate_vessel_co2(
            fuel_consumption=VESSELS[vessel]["fuel_consumption"],
            waiting_on_weather=VESSELS[vessel]["waiting_on_weather"],
            duration=VESSELS[vessel]["duration"],
            exposure=VESSELS[vessel]["exposure"],
            co2_per_fuel=VESSELS[vessel]["co2_per_fuel"],
        )
        == expected
    )


# v19.12.22
@pytest.mark.django_db
def test_calculate_step_vessel_fuel(vessel_uses: QuerySet[PlannedVesselUse]):
    assert (
        calculate_step_vessels_fuel(
            vessel_uses=vessel_uses,
            # 'Well Planning'!J54
            step_duration=9.56,
            # 'Well Planning'!G65
            season_duration=18.58,
            # 'Well Planning'!H65 but ignoring the quota obligation factor
        )
        == 165.4271044133477
    )


# v19.12.22
@pytest.mark.django_db
def test_calculate_step_vessel_co2(vessel_uses: QuerySet[PlannedVesselUse]):
    assert (
        calculate_step_vessels_co2(
            vessel_uses=vessel_uses,
            # 'Well Planning'!J54
            step_duration=9.56,
            # 'Well Planning'!G65
            season_duration=18.58,
            # 'Well Planning'!J65 but ignoring the quota obligation factor
        )
        == 524.4039209903123
    )
