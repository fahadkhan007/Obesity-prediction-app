# 🏥 Obesity Level Predictor

An AI-powered web application that predicts obesity levels based on lifestyle and physical characteristics using machine learning.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)

## 📋 Features

- **Beautiful UI**: Modern, gradient-based interface with smooth animations
- **Comprehensive Input**: Collects detailed information about:
  - Personal information (age, gender, height, weight)
  - Dietary habits (vegetable intake, meal frequency, snacking)
  - Lifestyle factors (water intake, smoking, alcohol)
  - Physical activity (exercise hours, screen time, transportation)
- **Real-time Predictions**: Instant obesity level classification
- **Smart Recommendations**: Personalized health advice based on predictions
- **BMI Calculator**: Automatic BMI calculation from height and weight

## 🎯 Prediction Categories

The model predicts one of the following obesity levels:
- Insufficient Weight
- Normal Weight
- Overweight Level I
- Overweight Level II
- Obesity Type I
- Obesity Type II
- Obesity Type III

## 🚀 Installation & Setup

### 1. Clone or Navigate to the Project Directory

```bash
cd d:\INT234project
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎮 Running the Application

### Start the Streamlit App

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Alternative: Specify Port

```bash
streamlit run app.py --server.port 8080
```

## 📁 Project Structure

```
INT234project/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
└── modelnb/
    ├── inference_pipeline.py       # Prediction logic
    ├── eda.ipynb                   # Exploratory Data Analysis
    ├── feature_engineering.ipynb   # Feature engineering notebook
    ├── model_Training.ipynb        # Model training notebook
    │
    ├── models/                     # Trained models and preprocessors
    │   ├── random_forest_model.pkl
    │   ├── label_encoders.pkl
    │   ├── target_label_encoder.pkl
    │   ├── robust_scaler.pkl
    │   └── feature_columns.pkl
    │
    └── *.csv                       # Dataset files
```

## 💻 Usage Guide

1. **Launch the Application**: Run `streamlit run app.py`
2. **Fill in Personal Information**:
   - Enter your age, gender, height, and weight
   - BMI will be calculated automatically
3. **Provide Dietary Habits**:
   - Family history of overweight
   - Food consumption patterns
   - Vegetable intake and meal frequency
4. **Enter Lifestyle Information**:
   - Water intake, smoking, and alcohol consumption
   - Calorie monitoring habits
5. **Add Physical Activity Details**:
   - Weekly exercise hours
   - Daily screen time
   - Primary transportation mode
6. **Click "Predict Obesity Level"**: Get instant results with personalized recommendations

## 🛠️ Technologies Used

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python 3.8+
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib

## 📊 Model Information

The prediction model uses:
- **Algorithm**: Random Forest Classifier
- **Features**: 18+ lifestyle and physical characteristics
- **Preprocessing**: Label encoding, one-hot encoding, robust scaling
- **Training Data**: Obesity dataset with synthetic data augmentation

## ⚠️ Disclaimer

This application is designed for **educational and informational purposes only**. The predictions should not be considered as medical advice. Please consult healthcare professionals for proper medical diagnosis and treatment.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📝 License

This project is open source and available for educational purposes.

## 📧 Support

For issues or questions, please create an issue in the project repository.

---

**Made with ❤️ using Streamlit and Machine Learning**
