from scapy.all import sniff, IP, TCP, UDP
import csv
import os
from datetime import datetime

from src.privacy.ip_sanitizer import IPSanitizer


CSV_FILE = "data/raw/network_traffic.csv"

sanitizer = IPSanitizer()   # MUST be global (important)


# Create CSV with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "src_ip",
            "dst_ip",
            "protocol",
            "src_port",
            "dst_port",
            "packet_size"
        ])


def process_packet(packet):

    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    real_src_ip = packet[IP].src
    real_dst_ip = packet[IP].dst

    # sanitize
    src_ip = sanitizer.sanitize(real_src_ip)
    dst_ip = sanitizer.sanitize(real_dst_ip)

    protocol = "OTHER"
    src_port = 0
    dst_port = 0

    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    packet_size = len(packet)

    print(
        f"[{protocol}] "
        f"{src_ip}:{src_port} -> {dst_ip}:{dst_port} | Size={packet_size}"
    )

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            packet_size
        ])


print("Starting Advanced Packet Capture...")
print("Press CTRL + C to stop.\n")

sniff(prn=process_packet, store=False)