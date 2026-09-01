# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Nobody has cleaned it up since.

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