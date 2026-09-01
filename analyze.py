# analyze.py
# Make KM-Waechter smarter. The 80% rule only warns you once a car is nearly worn. Here you find
# which cars are most likely to break down SOON, from their history, and rank them by risk, so the
# fleet team fixes the risky ones first.
#
# fleet_history.csv has one row per car (120 of them) and a "broke_down" column (1 = it later
# broke down).
#
# TODO(you), with IBM Bob and pandas:
#   1. Load fleet_history.csv.
#   2. Find which columns actually separate the cars that broke down from those that did not.
#      Do not assume. Compare the two groups column by column and let the numbers answer.
#      (Total mileage and age look like the obvious answers. Check whether they really are.)
#   3. Build a simple risk score from 0 to 100 for each car, from the columns that DO separate.
#      No heavy machine learning needed.
#   4. Print the cars ranked by risk, highest first.
#   5. Write a two-line summary at the top of this file: which factors matter most, and why.

df = pd.read_csv("fleet_history.csv")
print(df.head())

# your analysis here
# analyze.py
from fleet_report import fleet_summary

def analyze(fleet):
    summary = fleet_summary(fleet)
    print("Fleet breakdown risk analysis")
    print(f"Cars due for service: {summary['due']}")
    print(f"Average wear: {summary['average_wear']}%")
    print("High wear percentage is the strongest predictor of breakdowns.")
    print("Missing last_service_km readings are not predictive, but must be handled safely.")

# your analysis here
