import pandas as pd
import os

# File paths
INPUT_FILE = "data/raw/network_traffic.csv"
OUTPUT_FILE = "data/processed/network_features.csv"

print("Loading network traffic data...")

# Read CSV
df = pd.read_csv(INPUT_FILE)

print(f"Total packets loaded: {len(df)}")

# ----------------------------------
# Protocol Encoding
# ----------------------------------

protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "OTHER": 0
}

df["protocol_encoded"] = df["protocol"].map(protocol_map)

# ----------------------------------
# HTTPS Detection
# ----------------------------------

df["is_https"] = (
    (df["src_port"] == 443) |
    (df["dst_port"] == 443)
).astype(int)

# ----------------------------------
# DNS Detection
# ----------------------------------

df["is_dns"] = (
    (df["src_port"] == 53) |
    (df["dst_port"] == 53)
).astype(int)

# ----------------------------------
# Traffic Labels
# ----------------------------------

def classify_traffic(port):

    if port == 443:
        return "Browsing"

    elif port == 80:
        return "Browsing"

    elif port == 53:
        return "System"

    else:
        return "Unknown"


df["traffic_type"] = df["dst_port"].apply(classify_traffic)

# ----------------------------------
# Privacy Score
# ----------------------------------

def privacy_score(port):

    if port == 443:
        return 100

    elif port == 80:
        return 50

    else:
        return 30


df["privacy_score"] = df["dst_port"].apply(privacy_score)

# ----------------------------------
# Carbon Estimate
# ----------------------------------

df["traffic_mb"] = df["packet_size"] / (1024 * 1024)

df["carbon_estimate"] = (
    df["traffic_mb"] * 0.06
)

# ----------------------------------
# Save Processed Dataset
# ----------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nFeature Engineering Completed Successfully!")

print(f"Processed file saved to:\n{OUTPUT_FILE}")

print("\nFirst 5 Rows:\n")

print(
    df[
        [
            "packet_size",
            "protocol_encoded",
            "is_https",
            "is_dns",
            "traffic_type",
            "privacy_score",
            "carbon_estimate"
        ]
    ].head()
)