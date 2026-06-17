from src.analytics.summary import AnalyticsSummary

summary_engine = AnalyticsSummary("data/processed/ai_dataset.csv")

summary = summary_engine.generate_summary()

print(summary)