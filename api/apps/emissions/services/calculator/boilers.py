import logging

from apps.emissions.models import AssetSeason
from apps.emissions.models.assets import Baseline
from apps.wells.models import WellPlannerPlannedStep

logger = logging.getLogger(__name__)


# v19.12.22
# 'Calculation'!H307
def calculate_boilers_fuel(
    *,
    # 'Calculation!G307
    # fuel consumption in m3 per day
    fuel_consumption: float,
    # 'Calculation'!D256
    # planned duration in days
    duration: float,
) -> float:
    return fuel_consumption * duration


# v19.12.22
# 'Calculation'!J307
def calculate_boilers_co2(
    *,
    # 'Calculation!G307
    # fuel consumption in m3 per day
    fuel_consumption: float,
    # 'Calculation'!D256
    # planned duration in days
    duration: float,
    # 'Well Planning'!N11
    # ton of co2 per m3 of fuel
    co2_per_fuel: float,
) -> float:
    return (
        calculate_boilers_fuel(
            fuel_consumption=fuel_consumption,
            duration=duration,
        )
        * co2_per_fuel
    )


def get_boiler_fuel_consumption(baseline: Baseline, season: AssetSeason) -> float:
    match season:
        case AssetSeason.SUMMER:
            return baseline.boilers_fuel_consumption_summer
        case AssetSeason.WINTER:
            return baseline.boilers_fuel_consumption_winter

    raise ValueError(f"Unknown season: {season}")


# v19.12.22
def calculate_step_boilers_fuel(
    *,
    step: WellPlannerPlannedStep,
    duration: float,
) -> float:
    fuel_consumption = get_boiler_fuel_consumption(baseline=step.well_planner.baseline, season=step.season)  # type: ignore

    return calculate_boilers_fuel(
        fuel_consumption=fuel_consumption,
        duration=duration,
    )


# v19.12.22
def calculate_step_boilers_co2(
    *,
    step: WellPlannerPlannedStep,
    step_duration: float,
) -> float:
    fuel_consumption = get_boiler_fuel_consumption(baseline=step.well_planner.baseline, season=step.season)  # type: ignore

    return calculate_boilers_co2(
        fuel_consumption=fuel_consumption, duration=step_duration, co2_per_fuel=step.well_planner.boilers_co2_per_fuel
    )
