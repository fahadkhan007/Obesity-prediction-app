import streamlit as st
import sys
from pathlib import Path

# Add the modelnb directory to the path
sys.path.append(str(Path(__file__).parent / "modelnb"))

from modelnb.inference_pipeline import predict_obesity

# Page configuration
st.set_page_config(
    page_title="Obesity Level Predictor",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Obesity Level Predictor")
st.markdown("AI-Powered Health Assessment Tool")
st.divider()

# Sidebar
with st.sidebar:
    st.header("📊 About")
    st.info("This tool predicts obesity levels using machine learning based on lifestyle and physical characteristics.")
    
    st.header("🎯 Prediction Categories")
    st.markdown("""
    - Insufficient Weight
    - Normal Weight  
    - Overweight Level I
    - Overweight Level II
    - Obesity Type I
    - Obesity Type II
    - Obesity Type III
    """)
    
    st.warning("⚠️ Fill all the information (Personal info + Lifestyle + Physical Activity) to get the accurate prediction and suggestions.")

# Main form
st.header("Enter Your Information")

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["👤 Personal & Diet", "💧 Lifestyle", "🏃 Physical Activity"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        age = st.number_input("Age (years)", min_value=10, max_value=100, value=25, step=1)
        gender = st.selectbox("Gender", options=["Male", "Female"])
        height_m = st.number_input("Height (meters)", min_value=1.0, max_value=2.5, value=1.70, step=0.01, format="%.2f")
        weight_kg = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5, format="%.1f")
        
        # Calculate and display BMI
        bmi = weight_kg / (height_m ** 2)
        st.metric("Calculated BMI", f"{bmi:.2f}")
    
    with col2:
        st.subheader("Dietary Habits")
        family_overweight_history = st.selectbox("Family history of overweight?", options=["yes", "no"])
        high_calorie_food = st.selectbox("Frequent high-calorie food consumption?", options=["yes", "no"])
        vegetable_intake_freq = st.slider("Vegetable intake (times/day)", 0.0, 5.0, 2.0, 0.5)
        main_meals_per_day = st.slider("Main meals per day", 1.0, 5.0, 3.0, 0.5)
        snack_frequency = st.selectbox("Snacking frequency", options=["no", "Sometimes", "Frequently", "Always"])
        food_between_meals = st.selectbox("Food between meals", options=["no", "Sometimes", "Frequently", "Always"])

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Daily Habits")
        water_intake_liters = st.slider("Water intake (liters/day)", 0.5, 4.0, 2.0, 0.1)
        smokes = st.selectbox("Do you smoke?", options=["no", "yes"])
        calorie_tracking = st.selectbox("Do you monitor calorie consumption?", options=["no", "yes"])
    
    with col2:
        st.subheader("Alcohol Consumption")
        alcohol_consumption = st.selectbox("Alcohol consumption frequency", options=["no", "Sometimes", "Frequently", "Always"])

with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Exercise & Activity")
        physical_activity_hours = st.slider("Physical activity (hours/week)", 0.0, 20.0, 2.0, 0.5)
        screentime_hours = st.slider("Screen time (hours/day)", 0.0, 12.0, 4.0, 0.5)
    
    with col2:
        st.subheader("Transportation")
        travel_mode = st.selectbox(
            "Primary mode of transportation",
            options=["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"]
        )

st.divider()

# Prediction button
if st.button("🔮 Predict Obesity Level", type="primary", use_container_width=True):
    with st.spinner("Analyzing your data..."):
        try:
            # Prepare input data with EXACT field names from the CSV
            user_input = {
                "age": float(age),
                "gender": gender,
                "height_m": float(height_m),
                "weight_kg": float(weight_kg),
                "bmi": float(bmi),
                "family_overweight_history": family_overweight_history,
                "high_calorie_food": high_calorie_food,
                "vegetable_intake_freq": float(vegetable_intake_freq),
                "main_meals_per_day": float(main_meals_per_day),
                "snack_frequency": snack_frequency,
                "food_between_meals": food_between_meals,
                "smokes": smokes,  # Fixed: was "smoke"
                "water_intake_liters": float(water_intake_liters),
                "calorie_tracking": calorie_tracking,  # Fixed: was "calorie_monitoring"
                "physical_activity_hours": float(physical_activity_hours),
                "screentime_hours": float(screentime_hours),
                "travel_mode": travel_mode,
                "alcohol_consumption": alcohol_consumption
            }
            
            # Make prediction
            prediction = predict_obesity(user_input)
            
            # Display result
            st.success("✅ Prediction Complete!")
            st.markdown(f"### Your Predicted Obesity Level: **{prediction}**")
            
            # Provide recommendations
            st.divider()
            st.subheader("💡 Recommendations")
            
            if "Normal" in prediction:
                st.success("""
                **✅ Great! You're maintaining a healthy weight.**
                
                - Continue your current balanced lifestyle
                - Maintain regular physical activity (150+ minutes/week)
                - Keep eating a balanced diet with plenty of vegetables
                - Stay hydrated with adequate water intake
                """)
            elif "Insufficient" in prediction:
                st.warning("""
                **⚠️ You may be underweight.**
                
                - Increase calorie intake with nutritious, energy-dense foods
                - Include healthy fats (nuts, avocados, olive oil)
                - Consider strength training to build muscle mass
                - Consult a nutritionist for a personalized meal plan
                """)
            else:  # Overweight or Obesity
                st.error("""
                **🔴 Action recommended to improve your health.**
                
                - Aim for 150-300 minutes of moderate exercise per week
                - Reduce high-calorie food consumption
                - Increase vegetable and fiber intake
                - Drink at least 2 liters of water daily
                - Limit alcohol and sugary beverages
                - Consider consulting a healthcare professional
                - Track your daily calorie intake
                """)
                
        except Exception as e:
            st.error("❌ Error during prediction")
            st.error(f"Error message: {str(e)}")
            
            with st.expander("🔍 Debug Information"):
                st.write("**Input data:**")
                st.json(user_input)
                st.write("**Error details:**")
                st.code(str(e))
                st.write("**Troubleshooting tips:**")
                st.markdown("""
                1. Ensure all model files are in `modelnb/models/` directory
                2. Check that all dependencies are installed: `pip install -r requirements.txt`
                3. Verify the inference_pipeline.py is working correctly
                """)

# Footer
st.divider()
st.markdown("Made with ❤️ using Streamlit & Machine Learning by fahad khan")
