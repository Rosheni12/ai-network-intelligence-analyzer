from src.analytics.metrics import NetworkMetrics


class AnalyticsInsights:

    def __init__(self, dataset_path):
        self.metrics = NetworkMetrics(dataset_path)

    def generate_insights(self):

        insights = []

        # Network Health
        insights.append(
            f"Overall network health is {self.metrics.health_grade()}."
        )

        # HTTPS
        if self.metrics.https_percentage() >= 80:
            insights.append(
                "HTTPS adoption is excellent, indicating secure web communication."
            )
        else:
            insights.append(
                "HTTPS usage is relatively low and should be improved."
            )

        # Privacy
        if self.metrics.average_privacy_score() >= 70:
            insights.append(
                "Privacy score indicates good protection of user traffic."
            )
        else:
            insights.append(
                "Privacy score is below the recommended level."
            )

        # Risk
        insights.append(
            f"Current network risk level is {self.metrics.risk_level()}."
        )

        # Anomalies
        insights.append(
            f"{self.metrics.anomaly_percentage()}% of observed traffic was classified as anomalous."
        )

        # Sustainability
        if self.metrics.total_carbon() < 1:
            insights.append(
                "Estimated carbon footprint is low, indicating efficient network activity."
            )
        else:
            insights.append(
                "Carbon footprint is relatively high."
            )

        return insights