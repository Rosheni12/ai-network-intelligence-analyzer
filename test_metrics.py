from src.analytics.metrics import NetworkMetrics

metrics = NetworkMetrics("data/processed/ai_dataset.csv")

print("Total Packets:", metrics.total_packets())
print("Total Clients:", metrics.total_clients())
print("Total Traffic (MB):", metrics.total_traffic_mb())
print("Average Packet Size:", metrics.average_packet_size())
print("HTTPS %:", metrics.https_percentage())
print("DNS %:", metrics.dns_percentage())
print("Average Privacy Score:", metrics.average_privacy_score())
print("Total Carbon:", metrics.total_carbon())
print("\nTop Client:", metrics.top_client())

print("\nTop 5 Clients:")
print(metrics.top_5_clients())

print("\nTop Destination:", metrics.top_destination())

print("\nTop Protocol:", metrics.top_protocol())
print("\nProtocol Distribution:")
print(metrics.protocol_distribution())

print("\nTraffic Type Distribution:")
print(metrics.traffic_type_distribution())

print("\nPacket Category Distribution:")
print(metrics.packet_category_distribution())
print("\nAnomaly Count:", metrics.anomaly_count())
print("Normal Count:", metrics.normal_count())
print("Anomaly Percentage:", metrics.anomaly_percentage(), "%")