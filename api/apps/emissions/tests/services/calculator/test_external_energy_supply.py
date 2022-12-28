import pytest

from apps.emissions.factories import ExternalEnergySupplyFactory
from apps.emissions.services.calculator.external_energy_supply import (
    calculate_external_energy_supply_co2,
    calculate_external_energy_supply_co2_reduction,
    calculate_external_energy_supply_fuel_reduction,
    calculate_step_external_energy_supply_co2,
    calculate_step_external_energy_supply_co2_reduction,
    calculate_step_external_energy_supply_fuel_reduction,
)
from apps.wells.factories import WellPlannerPlannedStepFactory
from apps.wells.models import WellPlannerPlannedStep

# v19.12.2022
PHASES = {
    "Phase 2": dict(
        # 'Well Planning'!J5
        duration=6.13,
    ),
    "Phase 3": dict(
        # 'Well Planning'!J56
        duration=2.89,
    ),
}


# v19.12.2022
@pytest.fixture
def step() -> WellPlannerPlannedStep:
    external_energy_supply = ExternalEnergySupplyFactory(
        # 'Calculation'!D278
        capacity=4.0,
        # 'Calculation'!G278
        generator_efficiency_factor=3.881,
        # 'Asset & Material Inputs'!I97
        co2=0.055,
    )
    step = WellPlannerPlannedStepFactory(
        well_planner__asset=external_energy_supply.asset,
    )
    return step


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!H289
            1.3486,
        ),
        (
            "Phase 3",
            # 'Calculation'!H296
            0.6358,
        ),
    ),
)
def test_calculate_external_energy_supply_co2(phase: str, expected: float):
    assert (
        calculate_external_energy_supply_co2(
            # 'Calculation'!D278
            capacity=4.0,
            # 'Calculation'!E278
            co2_factor=0.055,
            duration=PHASES[phase]["duration"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!F289
            95.16211999999999,
        ),
        (
            "Phase 3",
            # 'Calculation'!H296
            44.86436,
        ),
    ),
)
def test_calculate_external_energy_supply_fuel_reduction(phase: str, expected: float):
    assert (
        calculate_external_energy_supply_fuel_reduction(
            # 'Calculation'!D278
            capacity=4.0,
            # 'Calculation'!G278
            generator_efficiency=3.881,
            duration=PHASES[phase]["duration"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!I213
            301.66392039999994,
        ),
        (
            "Phase 3",
            # 'Calculation'!I237
            142.2200212,
        ),
    ),
)
def test_calculate_external_energy_supply_co2_reduction(phase: str, expected: float):
    assert (
        calculate_external_energy_supply_co2_reduction(
            # 'Calculation'!D278
            capacity=4.0,
            # 'Calculation'!G278
            generator_efficiency=3.881,
            # 'Well Planning'!C11
            co2_per_fuel=3.17,
            duration=PHASES[phase]["duration"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!H289
            1.3486,
        ),
        (
            "Phase 3",
            # 'Calculation'!H296
            0.6358,
        ),
    ),
)
def test_calculate_step_energy_supply_co2(step: WellPlannerPlannedStep, phase: str, expected: float):
    assert (
        calculate_step_external_energy_supply_co2(
            step=step,
            step_duration=PHASES[phase]["duration"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!F289
            95.16211999999999,
        ),
        (
            "Phase 3",
            # 'Calculation'!H296
            44.86436,
        ),
    ),
)
def test_calculate_step_external_energy_supply_fuel_reduction(
    step: WellPlannerPlannedStep, phase: str, expected: float
):
    assert (
        calculate_step_external_energy_supply_fuel_reduction(
            step=step,
            step_duration=PHASES[phase]["duration"],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.2022
    (
        (
            "Phase 2",
            # 'Calculation'!I213
            301.66392039999994,
        ),
        (
            "Phase 3",
            # 'Calculation'!I237
            142.2200212,
        ),
    ),
)
def test_calculate_step_external_energy_supply_co2_reduction(step: WellPlannerPlannedStep, phase: str, expected: float):
    assert (
        calculate_step_external_energy_supply_co2_reduction(
            step=step,
            step_duration=PHASES[phase]["duration"],
        )
        == expected
    )
