import streamlit as st
from nlp_engine import extract_fitness_data
from nutrition_engine import calculate_nutrition
from activity_engine import calculate_burn
from bodytype_engine import recommend_strategy
from tdee_engine import calculate_bmr, calculate_tdee, recommend_calorie_target

st.set_page_config(page_title="IRONAI", layout="wide")

st.title("💪 IRONAI - AI Gym & Nutrition Assistant")

st.sidebar.header("👤 User Profile")

weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=100.0, max_value=220.0, value=170.0)
age = st.sidebar.number_input("Age", min_value=10, max_value=80, value=25)
gender = st.sidebar.selectbox("Gender", ["male", "female"])
activity_level = st.sidebar.selectbox("Activity Level",
                                       ["sedentary", "light", "moderate", "active", "very active"])
goal = st.sidebar.selectbox("Goal", ["maintain", "bulk", "cut"])

st.subheader("📝 Enter Your Daily Log")

prompt = st.text_area("Example: I ate 4 eggs and 2 rotis and did gym for 1 hour. I am endomorph.")

if st.button("Analyze"):

    parsed = extract_fitness_data(prompt)
    nutrition = calculate_nutrition(parsed["foods"])
    burned = calculate_burn(parsed["activities"], weight)
    net_calories = nutrition["calories"] - burned

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    target_calories = recommend_calorie_target(tdee, goal)

    difference = nutrition["calories"] - target_calories
    strategy = recommend_strategy(parsed["body_type"], net_calories)

    st.markdown("---")
    st.header("📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔥 Intake", f"{nutrition['calories']} kcal")
    col2.metric("🏃 Burned", f"{burned} kcal")
    col3.metric("⚖ Net", f"{net_calories} kcal")

    st.markdown("---")

    st.subheader("🧬 Metabolic Info")
    st.write(f"BMR: {round(bmr,2)} kcal")
    st.write(f"TDEE: {round(tdee,2)} kcal")
    st.write(f"Target Calories ({goal}): {round(target_calories,2)} kcal")

    st.subheader("🎯 Target Comparison")
    st.write(f"Difference from Target: {round(difference,2)} kcal")

    st.subheader("🧠 Strategy Suggestion")
    st.success(strategy)