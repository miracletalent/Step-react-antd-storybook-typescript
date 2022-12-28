from typing import TypedDict

from apps.wells.models import WellPlannerPlannedStep

from .assets import calculate_step_asset_co2
from .boilers import calculate_step_boilers_co2
from .external_energy_supply import calculate_step_external_energy_supply_co2
from .helicopters import calculate_step_helicopters_co2
from .materials import calculate_step_materials_co2
from .vessels import calculate_step_vessels_co2


class BaselineCO2Data(TypedDict):
    asset: float
    boilers: float
    vessels: float
    helicopters: float
    materials: float
    external_energy_supply: float


def calculate_planned_step_baseline_co2(
    *, planned_step: WellPlannerPlannedStep, step_duration: float, plan_duration: float, season_duration: float
) -> BaselineCO2Data:
    asset_co2 = calculate_step_asset_co2(step=planned_step, step_duration=step_duration)
    boilers_co2 = calculate_step_boilers_co2(step=planned_step, step_duration=step_duration)
    vessels_co2 = calculate_step_vessels_co2(
        vessel_uses=planned_step.well_planner.plannedvesseluse_set.filter(season=planned_step.season).select_related(
            'vessel_type'
        ),
        step_duration=step_duration,
        season_duration=season_duration,
    )
    helicopters_co2 = calculate_step_helicopters_co2(
        helicopter_uses=planned_step.well_planner.plannedhelicopteruse_set.select_related('helicopter_type'),
        step_duration=step_duration,
        plan_duration=plan_duration,
    )
    materials_co2 = calculate_step_materials_co2(materials=planned_step.materials.select_related('material_type'))

    if planned_step.external_energy_supply_enabled:
        external_energy_supply_co2 = calculate_step_external_energy_supply_co2(
            step=planned_step,
            step_duration=step_duration,
        )
    else:
        external_energy_supply_co2 = 0

    return BaselineCO2Data(
        asset=asset_co2,
        boilers=boilers_co2,
        vessels=vessels_co2,
        helicopters=helicopters_co2,
        materials=materials_co2,
        external_energy_supply=external_energy_supply_co2,
    )


def multiply_baseline_co2(
    baseline: BaselineCO2Data,
    multiplier: float,
) -> BaselineCO2Data:
    return BaselineCO2Data(
        asset=baseline['asset'] * multiplier,
        boilers=baseline['boilers'] * multiplier,
        vessels=baseline['vessels'] * multiplier,
        helicopters=baseline['helicopters'] * multiplier,
        materials=baseline['materials'] * multiplier,
        external_energy_supply=baseline['external_energy_supply'] * multiplier,
    )
