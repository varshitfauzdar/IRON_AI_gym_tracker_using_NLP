import json

with open("data/foods.json", "r") as f:
    FOOD_DB = json.load(f)

def calculate_nutrition(food_list):
    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fats": 0
    }

    for item in food_list:
        name = item["name"].rstrip("s")  # handle plural
        quantity = item["quantity"]

        if name in FOOD_DB:
            food_data = FOOD_DB[name]

            total["calories"] += food_data["calories"] * quantity
            total["protein"] += food_data["protein"] * quantity
            total["carbs"] += food_data["carbs"] * quantity
            total["fats"] += food_data["fats"] * quantity

    return total