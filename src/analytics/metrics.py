import os
import pandas as pd


class NetworkMetrics:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        anomaly_file = "data/processed/anomaly_results.csv"

        if os.path.exists(anomaly_file):
            self.anomaly_df = pd.read_csv(anomaly_file)
        else:
            self.anomaly_df = None

    def total_packets(self):
        return len(self.df)

    def total_clients(self):
        clients = set(self.df["src_ip"]).union(set(self.df["dst_ip"]))
        return len(clients)

    def total_traffic_mb(self):
        return round(self.df["traffic_mb"].sum(), 4)

    def average_packet_size(self):
        return round(self.df["packet_size"].mean(), 2)

    def https_percentage(self):
        return round((self.df["is_https"].mean()) * 100, 2)

    def dns_percentage(self):
        return round((self.df["is_dns"].mean()) * 100, 2)

    def average_privacy_score(self):
        return round(self.df["privacy_score"].mean(), 2)

    def total_carbon(self):
        return round(self.df["carbon_estimate"].sum(), 6)
        
    def top_client(self):
        return self.df["src_ip"].value_counts().idxmax()

    def top_5_clients(self):
        return self.df["src_ip"].value_counts().head(5)

    def top_destination(self):
        return self.df["dst_ip"].value_counts().idxmax()

    def top_protocol(self):
        return self.df["protocol"].value_counts().idxmax()
        
    def protocol_distribution(self):
        return self.df["protocol"].value_counts()

    def traffic_type_distribution(self):
        return self.df["traffic_type"].value_counts()

    def packet_category_distribution(self):
        return self.df["packet_category"].value_counts()   
    
    def anomaly_count(self):
        if self.anomaly_df is None:
            return 0

        return len(
            self.anomaly_df[
                self.anomaly_df["anomaly_status"] == "ANOMALY"
            ]
        )

    def normal_count(self):
        if self.anomaly_df is None:
            return 0

        return len(
            self.anomaly_df[
                self.anomaly_df["anomaly_status"] == "NORMAL"
            ]
        )

    def anomaly_percentage(self):
        if self.anomaly_df is None:
            return 0

        total = len(self.anomaly_df)

        if total == 0:
            return 0

        anomalies = self.anomaly_count()

        return round((anomalies / total) * 100, 2)
    
    def network_health_score(self):
        https = self.https_percentage()
        privacy = self.average_privacy_score()
        anomaly = self.anomaly_percentage()

    # Convert carbon footprint into a score (0–100)
        carbon = self.total_carbon()
        carbon_score = max(0, 100 - (carbon * 100))

        score = (
            (https * 0.40)
            + (privacy * 0.30)
            + ((100 - anomaly) * 0.20)
            + (carbon_score * 0.10)
    )
    
        return round(score, 2)
    
    def risk_level(self):
        anomaly = self.anomaly_percentage()

        if anomaly < 5:
           return "LOW"

        elif anomaly < 15:
            return "MEDIUM"

        else:
            return "HIGH"


    def health_grade(self):
        score = self.network_health_score()

        if score >= 90:
             return "Excellent"

        elif score >= 75:
            return "Good"

        elif score >= 60:
            return "Fair"

        else:
            return "Poor"


    def network_status(self):
        grade = self.health_grade()
        risk = self.risk_level()

        if grade in ["Excellent", "Good"] and risk == "LOW":
            return "🟢 HEALTHY"

        elif risk == "MEDIUM":
            return "🟡 WARNING"

        else:
             return "🔴 CRITICAL" 