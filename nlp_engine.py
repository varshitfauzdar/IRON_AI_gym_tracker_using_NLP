import re

# Map plural → singular
FOOD_KEYWORDS = {
    "eggs": "egg",
    "egg": "egg",
    "rotis": "roti",
    "roti": "roti",
    "rice": "rice",
    "chicken": "chicken",
    "milk": "milk"
}

ACTIVITY_KEYWORDS = ["gym", "running", "swimming", "football", "cycling"]

BODY_TYPES = ["endomorph", "ectomorph", "mesomorph"]

def extract_fitness_data(text):
    text = text.lower()

    foods = []
    activities = []
    body_type = None

    # Extract body type
    for bt in BODY_TYPES:
        if bt in text:
            body_type = bt

    # Extract food quantities properly
    pattern = r'(\d+)\s+(eggs?|rotis?|rice|chicken|milk)'
    matches = re.findall(pattern, text)

    for quantity, food_name in matches:
        canonical_name = FOOD_KEYWORDS[food_name]
        foods.append({
            "name": canonical_name,
            "quantity": int(quantity)
        })

    # Extract activity duration
    duration_pattern = r'(\d+)\s*(hour|hours|hr|hrs|minutes|min)'
    durations = re.findall(duration_pattern, text)

    for activity in ACTIVITY_KEYWORDS:
        if activity in text:
            duration = None
            if durations:
                value, unit = durations[0]
                duration = f"{value} {unit}"
            activities.append({
                "name": activity,
                "duration": duration
            })

    return {
        "foods": foods,
        "activities": activities,
        "body_type": body_type
    }