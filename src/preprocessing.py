import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/student_exam_performance.csv")

print("Original Dataset:")
print(df.head())

# Remove missing values
df = df.dropna()

# Create risk category
def risk_category(score):
    if score < 50:
        return "High Risk"
    elif score < 75:
        return "Medium Risk"
    else:
        return "Low Risk"

# Add new column
df["Risk_Level"] = df["Final_Exam_Score"].apply(risk_category)

# Encode categorical columns
le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    if col != "Risk_Level":
        df[col] = le.fit_transform(df[col])

# Save processed dataset
df.to_csv("data/processed_data.csv", index=False)

print("processed_data.csv created successfully!")