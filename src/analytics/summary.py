import json
from src.analytics.metrics import NetworkMetrics


class AnalyticsSummary:

    def __init__(self, dataset_path):
        self.metrics = NetworkMetrics(dataset_path)

    def generate_summary(self):

        summary = {
            "total_packets": self.metrics.total_packets(),
            "total_clients": self.metrics.total_clients(),
            "total_traffic_mb": self.metrics.total_traffic_mb(),
            "average_packet_size": self.metrics.average_packet_size(),
            "https_percentage": self.metrics.https_percentage(),
            "dns_percentage": self.metrics.dns_percentage(),
            "privacy_score": self.metrics.average_privacy_score(),
            "carbon_footprint": self.metrics.total_carbon(),
            "top_client": self.metrics.top_client(),
            "top_protocol": self.metrics.top_protocol(),
            "anomaly_count": self.metrics.anomaly_count(),
            "normal_count": self.metrics.normal_count(),
            "anomaly_percentage": self.metrics.anomaly_percentage(),
            "protocol_distribution": self.metrics.protocol_distribution().to_dict(),
            "traffic_type_distribution": self.metrics.traffic_type_distribution().to_dict(),
            "packet_category_distribution": self.metrics.packet_category_distribution().to_dict(),
            "network_health_score": self.metrics.network_health_score(),
            "risk_level": self.metrics.risk_level(),
            "health_grade": self.metrics.health_grade(),
            "network_status": self.metrics.network_status(),
        }

        return summary

    def save_summary(self, output_path="data/processed/summary.json"):

        summary = self.generate_summary()

        with open(output_path, "w") as f:
            json.dump(summary, f, indent=4)

        print("\nSummary saved to:", output_path)