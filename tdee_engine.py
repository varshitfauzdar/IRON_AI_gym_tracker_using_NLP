def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161


def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }

    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    return bmr * multiplier


def recommend_calorie_target(tdee, goal):
    if goal == "bulk":
        return tdee + 300
    elif goal == "cut":
        return tdee - 400
    else:
        return tdee