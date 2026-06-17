import pandas as pd
from src.capture.features.feature_engine import FeatureEngineer

INPUT_FILE = "data/raw/network_traffic.csv"
OUTPUT_FILE = "data/processed/ai_dataset.csv"

print("Loading raw dataset...")

df = pd.read_csv(INPUT_FILE)

print("Total packets:", len(df))

engineer = FeatureEngineer()
df = engineer.transform(df)

print("Feature engineering complete!")

df.to_csv(OUTPUT_FILE, index=False)

print("Saved to:", OUTPUT_FILE)
print(df.head())