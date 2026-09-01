# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Nobody has cleaned it up since.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: int, interval: int) -> float:
     """Return wear percentage of the service interval used."""
     ratio = km_since_service / interval
     return ratio * 100.0
    """Return wear percentage of the service interval used."""
    ratio = km_since_service / interval
    return ratio * 100.0


def needs_service(car: dict) -> bool:
     """Check if a car needs service based on odometer and last service reading."""
     if "last_service_km" not in car:
         return False  # no reading, cannot flag
     km_since = car["odometer"] - car["last_service_km"]
     pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
     return pct >= WARN_AT_PERCENT
        return True
    else:
        return False
    """Check if a car needs service based on odometer and last service reading."""
    if "last_service_km" not in car:
        return False  # no reading, cannot flag
    km_since = car["odometer"] - car["last_service_km"]
    pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
    return pct >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list[str]:
     """Check all cars in the fleet and return IDs of those needing service."""
     flagged: list[str] = []
     for car in fleet:
         if needs_service(car):
             flagged.append(car["id"])
             print(f"SERVICE DUE: {car['id']}")
     return flagged
    """Check all cars in the fleet and return IDs of those needing service."""
    flagged: list[str] = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged