import pytest

from apps.emissions.factories import BaselineInputFactory
from apps.emissions.services.calculator.assets import (
    calculate_asset_co2,
    calculate_asset_fuel,
    calculate_step_asset_co2,
    calculate_step_asset_fuel,
)
from apps.wells.factories import WellPlannerPlannedStepFactory

# v19.12.22
PHASES = {
    "Phase 1": dict(
        # 'Well Planning'!H54
        baseline_fuel=130.0,
        # 'Well Planning'!I54
        duration=9.55,
    ),
    "Phase 2": dict(
        # 'Well Planning'!H55
        baseline_fuel=128.75,
        # 'Well Planning'!I55
        duration=7.67,
    ),
    "Phase 3": dict(
        # 'Well Planning'!H56
        baseline_fuel=128.75,
        # 'Well Planning'!I56
        duration=3.36,
    ),
}


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!D6
        ("Phase 1", 1241.5),
        # 'Calculation'!E6
        ("Phase 2", 987.5125),
        # 'Calculation'!F6
        ("Phase 3", 432.59999999999997),
    ),
)
def test_calculate_asset_fuel(
    phase: str,
    expected: float,
):
    assert (
        calculate_asset_fuel(
            baseline_fuel=PHASES[phase]['baseline_fuel'],
            duration=PHASES[phase]['duration'],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!D24
        ("Phase 1", 3935.555),
        # 'Calculation'!E24
        ("Phase 2", 3130.414625),
        # 'Calculation'!F24
        ("Phase 3", 1371.3419999999999),
    ),
)
def test_calculate_asset_co2(
    phase: str,
    expected: float,
):
    assert (
        calculate_asset_co2(
            baseline_fuel=PHASES[phase]['baseline_fuel'],
            duration=PHASES[phase]['duration'],
            co2_per_fuel=3.17,
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!D6
        ("Phase 1", 1241.5),
        # 'Calculation'!E6
        ("Phase 2", 987.5125),
        # 'Calculation'!F6
        ("Phase 3", 432.59999999999997),
    ),
)
def test_calculate_step_asset_fuel(
    phase: str,
    expected: float,
):
    step = WellPlannerPlannedStepFactory()
    BaselineInputFactory(
        baseline=step.well_planner.baseline,
        phase=step.phase,
        mode=step.mode,
        value=PHASES[phase]['baseline_fuel'],
    )
    BaselineInputFactory()

    assert (
        calculate_step_asset_fuel(
            step=step,
            step_duration=PHASES[phase]['duration'],
        )
        == expected
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'phase,expected',
    # v19.12.22
    (
        # 'Calculation'!D24
        ("Phase 1", 3935.555),
        # 'Calculation'!E24
        ("Phase 2", 3130.414625),
        # 'Calculation'!F24
        ("Phase 3", 1371.3419999999999),
    ),
)
def test_calculate_step_asset_co2(
    phase: str,
    expected: float,
):
    step = WellPlannerPlannedStepFactory()
    BaselineInputFactory(
        baseline=step.well_planner.baseline,
        phase=step.phase,
        mode=step.mode,
        value=PHASES[phase]['baseline_fuel'],
    )
    BaselineInputFactory()

    assert (
        calculate_step_asset_co2(
            step=step,
            step_duration=PHASES[phase]['duration'],
        )
        == expected
    )
