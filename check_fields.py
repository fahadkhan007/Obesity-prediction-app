import joblib
import pandas as pd

print("=" * 50)
print("CHECKING MODEL REQUIREMENTS")
print("=" * 50)

# Load label encoders
label_encoders = joblib.load("modelnb/models/label_encoders.pkl")
print("\nLabel Encoder Keys (fields that need encoding):")
for key in label_encoders.keys():
    print(f"  - {key}")

# Load feature columns
feature_columns = joblib.load("modelnb/models/feature_columns.pkl")
print(f"\nTotal Feature Columns: {len(feature_columns)}")
print("\nAll Feature Columns:")
for col in feature_columns:
    print(f"  - {col}")

# Check CSV columns
df = pd.read_csv("modelnb/obesity_data_cleaned.csv")
print(f"\nCSV Columns ({len(df.columns)} total):")
for col in df.columns:
    print(f"  - {col}")

print("\n" + "=" * 50)
