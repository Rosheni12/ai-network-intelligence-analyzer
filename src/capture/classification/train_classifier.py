import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

INPUT_FILE = "data/processed/ai_dataset.csv"

print("Loading processed dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Total samples: {len(df)}")

# -----------------------------
# Features
# -----------------------------

X = df[
    [
        "packet_size",
        "protocol_encoded",
        "traffic_mb",
        "carbon_estimate"
    ]
]

# -----------------------------
# Target
# -----------------------------

y = df["traffic_type"]

# -----------------------------
# Train/Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Random Forest...\n")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("=" * 50)
print(f"Accuracy : {accuracy:.4f}")
print("=" * 50)

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, predictions))

# -----------------------------
# Save Model
# -----------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/traffic_classifier.pkl"
)

print("\nModel saved successfully!")

print("models/traffic_classifier.pkl")