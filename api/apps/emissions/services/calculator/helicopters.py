from django.db.models import QuerySet

from apps.emissions.models import BaseHelicopterUse


# v19.12.22
# 'Calculation'!F115
def calculate_helicopter_fuel(
    *,
    # 'Well Planning'!O19
    # duration of roundtrip in minutes
    roundtrip_minutes: float,
    # 'Well Planning'!P19
    # number of roundtrips
    roundtrip_count: int,
    # 'Asset & Materials Input'!F86
    # fuel consumption in liters per hour
    fuel_consumption: float,
    # 'Well Planning'!Q19
    # exposure against current well in percentage
    exposure: float,
) -> float:
    return (roundtrip_minutes / 60) * roundtrip_count * (fuel_consumption / 1000) * (exposure / 100)


# v19.12.22
# 'Calculation'!H115
def calculate_helicopter_co2(
    *,
    # 'Well Planning'!O19
    # duration of roundtrip in minutes
    roundtrip_minutes: float,
    # 'Well Planning'!P19
    # number of roundtrips
    roundtrip_count: int,
    # 'Asset & Materials Input'!F86
    # fuel consumption in liters per hour
    fuel_consumption: float,
    # 'Well Planning'!Q19
    # exposure against current well in percentage
    exposure: float,
    # 'Asset & Materials Input'!G86
    # tons of co2 per m3 of fuel
    co2_per_fuel: float,
) -> float:
    return (
        calculate_helicopter_fuel(
            roundtrip_minutes=roundtrip_minutes,
            roundtrip_count=roundtrip_count,
            fuel_consumption=fuel_consumption,
            exposure=exposure,
        )
        * co2_per_fuel
    )


# v19.12.22
# 'Calculation'!F124
def calculate_step_helicopters_fuel(
    *, helicopter_uses: QuerySet[BaseHelicopterUse], step_duration: float, plan_duration: float
) -> float:
    return sum(
        calculate_helicopter_fuel(
            roundtrip_minutes=helicopter_use.trip_duration,
            roundtrip_count=helicopter_use.trips,
            fuel_consumption=helicopter_use.helicopter_type.fuel_consumption,
            exposure=helicopter_use.exposure_against_current_well,
        )
        * step_duration
        / plan_duration
        for helicopter_use in helicopter_uses
    )


# v19.12.22
# 'Calculation'!H124
def calculate_step_helicopters_co2(
    *,
    helicopter_uses: QuerySet[BaseHelicopterUse],
    step_duration: float,
    plan_duration: float,
) -> float:
    return sum(
        calculate_helicopter_co2(
            roundtrip_minutes=helicopter_use.trip_duration,
            roundtrip_count=helicopter_use.trips,
            fuel_consumption=helicopter_use.helicopter_type.fuel_consumption,
            exposure=helicopter_use.exposure_against_current_well,
            co2_per_fuel=helicopter_use.helicopter_type.co2_per_fuel,
        )
        * step_duration
        / plan_duration
        for helicopter_use in helicopter_uses
    )
