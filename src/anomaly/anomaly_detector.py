import pandas as pd
from sklearn.ensemble import IsolationForest

print("Loading processed dataset...")

df = pd.read_csv("data/processed/ai_dataset.csv")

# Features used for anomaly detection
features = df[
    [
        "packet_size",
        "protocol_encoded",
        "is_https",
        "is_dns"
    ]
]

print(f"Total packets: {len(df)}")

print("Training Isolation Forest...")

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(features)

# Predict anomalies
predictions = model.predict(features)

df["anomaly"] = predictions

df["anomaly_status"] = df["anomaly"].map({
    1: "NORMAL",
    -1: "ANOMALY"
})

output_file = "data/processed/anomaly_results.csv"

df.to_csv(output_file, index=False)

print("\nDetection Complete!")

print(df["anomaly_status"].value_counts())

print(f"\nResults saved to:\n{output_file}")