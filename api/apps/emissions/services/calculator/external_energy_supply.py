from apps.wells.models import BaseWellPlannerStep


# v19.12.2022
# 'Calculation'!H289
def calculate_external_energy_supply_co2(
    *,
    # 'Calculation'!D278
    capacity: float,
    # 'Calculation'!E278
    co2_factor: float,
    # 'Well Planning'!J55
    duration: float,
) -> float:
    return capacity * co2_factor * duration


# v19.12.2022
# 'Calculation'!F289
def calculate_external_energy_supply_fuel_reduction(
    *,
    # 'Calculation'!D278
    capacity: float,
    # 'Calculation'!G278
    generator_efficiency: float,
    # 'Well Planning'!J55,
    duration: float,
) -> float:
    return capacity * generator_efficiency * duration


# v19.12.2022
def calculate_external_energy_supply_co2_reduction(
    *,
    # 'Calculation'!D278
    capacity: float,
    # 'Calculation'!G278
    generator_efficiency: float,
    # 'Well Planning'!J55,
    duration: float,
    # 'Well Planning'!C11
    co2_per_fuel: float,
) -> float:
    return (
        calculate_external_energy_supply_fuel_reduction(
            capacity=capacity,
            generator_efficiency=generator_efficiency,
            duration=duration,
        )
        * co2_per_fuel
    )


# v19.12.2022
def calculate_step_external_energy_supply_co2(
    *,
    step: BaseWellPlannerStep,
    step_duration: float,
) -> float:
    external_energy_supply = step.well_planner.asset.external_energy_supply

    return calculate_external_energy_supply_co2(
        capacity=external_energy_supply.capacity,
        co2_factor=external_energy_supply.co2,
        duration=step_duration,
    )


# v19.12.2022
def calculate_step_external_energy_supply_fuel_reduction(
    *,
    step: BaseWellPlannerStep,
    step_duration: float,
) -> float:
    external_energy_supply = step.well_planner.asset.external_energy_supply

    return calculate_external_energy_supply_fuel_reduction(
        capacity=external_energy_supply.capacity,
        generator_efficiency=external_energy_supply.generator_efficiency_factor,
        duration=step_duration,
    )


# v19.12.2022
def calculate_step_external_energy_supply_co2_reduction(
    *,
    step: BaseWellPlannerStep,
    step_duration: float,
) -> float:
    external_energy_supply = step.well_planner.asset.external_energy_supply

    return calculate_external_energy_supply_co2_reduction(
        capacity=external_energy_supply.capacity,
        generator_efficiency=external_energy_supply.generator_efficiency_factor,
        duration=step_duration,
        co2_per_fuel=step.well_planner.co2_per_fuel,
    )
