import logging

import pytest

from apps.emissions.models.assets import AssetSeason
from apps.emissions.services.calculator.boilers import (
    calculate_boilers_co2,
    calculate_boilers_fuel,
    calculate_step_boilers_co2,
    calculate_step_boilers_fuel,
)
from apps.wells.factories import WellPlannerPlannedStepFactory

logger = logging.getLogger(__name__)


PHASES = {
    "Phase 1": dict(
        # 'Calculation'!G307
        fuel_consumption=1.0,
        # 'Well Planning'!J54
        duration=9.55,
        # 'Well Planning'!F54
        season=AssetSeason.SUMMER,
    ),
    "Phase 2": dict(
        # 'Calculation'!G315
        fuel_consumption=1.5,
        # 'Well Planning'!J55
        duration=6.13,
        # 'Well Planning'!F55
        season=AssetSeason.WINTER,
    ),
    "Phase 3": dict(
        # 'Calculation'!G323
        fuel_consumption=1.5,
        # 'Well Planning'!J56
        duration=2.89,
        # 'Well Planning'!F56
        season=AssetSeason.WINTER,
    ),
}


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!H307
        ("Phase 1", 9.55),
        # 'Calculation'!H315
        ("Phase 2", 9.195),
        # 'Calculation'!H323
        ("Phase 3", 4.335),
    ),
)
def test_calculate_boilers_fuel(phase: str, expected: float):
    assert (
        calculate_boilers_fuel(
            fuel_consumption=PHASES[phase]['fuel_consumption'],
            duration=PHASES[phase]['duration'],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!J307
        ("Phase 1", 30.273500000000002),
        # 'Calculation'!J315
        ("Phase 2", 29.14815),
        # 'Calculation'!J323
        ("Phase 3", 13.74195),
    ),
)
def test_calculate_boilers_co2(phase: str, expected: float):
    assert (
        calculate_boilers_co2(
            fuel_consumption=PHASES[phase]['fuel_consumption'],
            duration=PHASES[phase]['duration'],
            # 'Well Planning'!N11
            co2_per_fuel=3.17,
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!H307
        ("Phase 1", 9.55),
        # 'Calculation'!H315
        ("Phase 2", 9.195),
        # 'Calculation'!H323
        ("Phase 3", 4.335),
    ),
)
def test_calculate_step_boilers_fuel(phase: str, expected: float):
    step = WellPlannerPlannedStepFactory(
        season=PHASES[phase]["season"],
        # 'Asset Planning'!D50
        well_planner__baseline__boilers_fuel_consumption_summer=1.0,
        # 'Asset Planning'!E50
        well_planner__baseline__boilers_fuel_consumption_winter=1.5,
    )

    assert calculate_step_boilers_fuel(step=step, duration=PHASES[phase]["duration"]) == expected


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!J307
        ("Phase 1", 30.273500000000002),
        # 'Calculation'!J315
        ("Phase 2", 29.14815),
        # 'Calculation'!J323
        ("Phase 3", 13.74195),
    ),
)
def test_calculate_step_boilers_co2(phase: str, expected: float):
    step = WellPlannerPlannedStepFactory(
        season=PHASES[phase]["season"],
        # 'Well Planning'!N11
        well_planner__boilers_co2_per_fuel=3.17,
        # 'Asset Planning'!D50
        well_planner__baseline__boilers_fuel_consumption_summer=1.0,
        # 'Asset Planning'!E50
        well_planner__baseline__boilers_fuel_consumption_winter=1.5,
    )

    assert calculate_step_boilers_co2(step=step, step_duration=PHASES[phase]["duration"]) == expected
