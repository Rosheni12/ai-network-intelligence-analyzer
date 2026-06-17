from src.analytics.insights import AnalyticsInsights

engine = AnalyticsInsights("data/processed/ai_dataset.csv")

for insight in engine.generate_insights():
    print("•", insight)