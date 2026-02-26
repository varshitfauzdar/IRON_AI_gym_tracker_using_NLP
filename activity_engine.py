import json

with open("data/activities.json", "r") as f:
    ACTIVITY_DB = json.load(f)

def convert_to_hours(duration_str):
    if not duration_str:
        return 0

    value, unit = duration_str.split()
    value = float(value)

    if "hour" in unit or "hr" in unit:
        return value
    elif "min" in unit:
        return value / 60
    else:
        return 0

def calculate_burn(activities, weight):
    total_burn = 0

    for activity in activities:
        name = activity["name"]
        duration = convert_to_hours(activity["duration"])

        if name in ACTIVITY_DB:
            met = ACTIVITY_DB[name]
            burn = met * weight * duration
            total_burn += burn

    return round(total_burn, 2)