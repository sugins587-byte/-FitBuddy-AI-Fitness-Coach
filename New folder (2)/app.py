import streamlit as st
import google.generativeai as genai

# Config
st.set_page_config(page_title="FitBuddy - AI Fitness Plan", page_icon="💪")
st.title("💪 FitBuddy - AI Fitness Plan Generator")
st.write("Using Google Gemini Models")

# Get API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # User Inputs
    st.header("Enter Your Details")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 10, 100, 22)
        weight = st.number_input("Weight (kg)", 30, 200, 65)
        height = st.number_input("Height (cm)", 100, 250, 170)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col2:
        goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Stay Fit", "Endurance"])
        level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
        days = st.slider("Workout Days per Week", 2, 7, 5)
        diet_type = st.selectbox("Diet Preference", ["Veg", "Non-Veg", "Vegan", "Eggetarian"])

    if st.button("Generate My Fitness Plan"):
        with st.spinner("FitBuddy is creating your plan..."):
            prompt = f"""
            You are FitBuddy, an expert AI fitness coach.
            Create a detailed personalized fitness plan for:
            Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm
            Goal: {goal}, Level: {level}, Workout Days: {days} per week, Diet: {diet_type}
            
            Provide:
            1. Weekly Workout Schedule (with exercises, sets, reps)
            2. Daily Diet Plan (calories, protein)
            3. Tips for {goal}
            Make it simple and motivational.
            """
            response = model.generate_content(prompt)
            st.success("Your Personalized Plan is Ready!")
            st.markdown(response.text)
else:
    st.warning("Please enter Gemini API Key in sidebar to continue.")
    st.info("Get key from: https://aistudio.google.com/app/apikey")