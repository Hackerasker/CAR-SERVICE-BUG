# fleet_report.py
# Prints the nightly fleet-health summary for Vossberg Mobility.
# Written in 2014. Runs every morning. Never cleaned up.

# fleet_report.py
# Prints the nightly fleet-health summary for Vossberg Mobility.
# Written in 2014. Runs every morning. Never cleaned up.
# Written in 2014. Runs every morning. Cleaned up in 2026.

from km_wachter import wear_percent, needs_service, SERVICE_INTERVAL_KM
from config_loader import load_settings, get_setting
from log_util import log, flush_log
import fleet_utils 
import fleet_utils


def car_wear(car: dict) -> float:
     """Return wear percentage for a car, or 0 if no reading."""
     if "last_service_km" not in car:
         return 0.0
     return wear_percent(car["odometer"] - car["last_service_km"], SERVICE_INTERVAL_KM)
    """Return wear percentage for a car, or 0 if no reading."""
    if "last_service_km" not in car:
        return 0.0
    return wear_percent(car["odometer"] - car["last_service_km"], SERVICE_INTERVAL_KM)


def fleet_summary(fleet: list[dict]) -> dict:
     """Summarize fleet health: count, due, average wear."""
     total = 0.0
     due = 0
     valid_cars = 0
     for car in fleet:
         wear = car_wear(car)
         if wear > 0:
             total += wear
             valid_cars += 1
         if needs_service(car):
             due += 1
     average = round(total / valid_cars, 1) if valid_cars > 0 else 0.0
     return {"count": len(fleet), "due": due, "average_wear": average}
    """Summarize fleet health: count, due, average wear."""
    total = 0.0
    due = 0
    valid_cars = 0
    for car in fleet:
        wear = car_wear(car)
        if wear > 0:
            total += wear
            valid_cars += 1
        if needs_service(car):
            due += 1
    average = round(total / valid_cars, 1) if valid_cars > 0 else 0.0
    return {"count": len(fleet), "due": due, "average_wear": average}


def print_report(fleet: list[dict]) -> None:
    """Print nightly fleet report."""
     settings = load_settings()
     log(get_setting(settings, "report_title", "Nightly fleet report"))
     s = fleet_summary(fleet)
     print(f"Fleet: {s['count']} cars")
     print(f"Due for service: {s['due']}")
     print(f"Average wear: {s['average_wear']}%")
     total_km = sum(car["odometer"] for car in fleet)
     # Partner garage in England wants distance in miles (since 2015).
     miles = fleet_utils.km_to_miles(total_km)
     print(f"Fleet distance: {fleet_utils.format_number(miles)} miles")
     flush_log(get_setting(settings, "log_file", "km_wachter.log"))
    settings = load_settings()
    log(get_setting(settings, "report_title", "Nightly fleet report"))
    s = fleet_summary(fleet)
    print(f"Fleet: {s['count']} cars")
    print(f"Due for service: {s['due']}")
    print(f"Average wear: {s['average_wear']}%")
    total_km = sum(car["odometer"] for car in fleet)
    # Partner garage in England wants distance in miles (since 2015).
    miles = fleet_utils.km_to_miles(total_km)
    print(f"Fleet distance: {fleet_utils.format_number(miles)} miles")
    flush_log(get_setting(settings, "log_file", "km_wachter.log"))