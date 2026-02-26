def recommend_strategy(body_type, net_calories):
    if not body_type:
        return "Body type not specified. Unable to suggest strategy."

    body_type = body_type.lower()

    if body_type == "ectomorph":
        if net_calories < 300:
            return "You should increase calories. Aim for +300 to +500 kcal surplus for muscle gain."
        else:
            return "Good surplus for bulking."

    elif body_type == "mesomorph":
        if net_calories < 200:
            return "Consider mild surplus (+200 kcal) for lean muscle."
        elif net_calories > 500:
            return "Surplus too high. Risk of fat gain."
        else:
            return "Balanced intake."

    elif body_type == "endomorph":
        if net_calories > 0:
            return "You should maintain calorie deficit for fat loss."
        else:
            return "Good deficit for fat reduction."

    return "Invalid body type."