import joblib
import pandas as pd

# Load trained model
model = joblib.load(
    "models/traffic_classifier.pkl"
)

print("AI Model Loaded Successfully!\n")

# Sample packet data
sample_packet = pd.DataFrame([
    {
        "packet_size": 100,
        "protocol_encoded": 1,   # TCP
        "is_https": 1,
        "is_dns": 0
    }
])

prediction = model.predict(
    sample_packet
)

print("Packet Features:")
print(sample_packet)

print("\nAI Prediction:")
print(prediction[0])