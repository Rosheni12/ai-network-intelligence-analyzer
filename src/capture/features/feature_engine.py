import pandas as pd


class FeatureEngineer:

    def __init__(self):
        pass

    def transform(self, df):

        # ----------------------------------------
        # 1. Protocol Encoding
        # ----------------------------------------

        protocol_map = {
            "TCP": 1,
            "UDP": 2
        }

        df["protocol_encoded"] = (
            df["protocol"]
            .map(protocol_map)
            .fillna(0)
            .astype(int)
        )

        # ----------------------------------------
        # 2. HTTPS Detection
        # ----------------------------------------

        df["is_https"] = (
            (df["src_port"] == 443) |
            (df["dst_port"] == 443)
        ).astype(int)

        # ----------------------------------------
        # 3. DNS Detection
        # ----------------------------------------

        df["is_dns"] = (
            (df["src_port"] == 53) |
            (df["dst_port"] == 53)
        ).astype(int)

        # ----------------------------------------
        # 4. Packet Direction
        # ----------------------------------------

        df["direction"] = df.apply(
            lambda row: "Incoming"
            if row["src_port"] == 443
            else "Outgoing",
            axis=1
        )

        # ----------------------------------------
        # 5. Traffic Type Label Engine
        # ----------------------------------------

        def classify(row):

            protocol = row["protocol"]
            sport = row["src_port"]
            dport = row["dst_port"]
            size = row["packet_size"]

            # DNS
            if sport == 53 or dport == 53:
                return "System"

            # HTTPS browsing
            elif dport == 443 and size < 600:
                return "Browsing"

            # Large HTTPS downloads/uploads
            elif dport == 443 and size >= 600:
                return "Communication"

            # HTTP
            elif dport in [80, 8080]:
                return "Browsing"

            # SSH
            elif dport == 22:
                return "System"

            # Email
            elif dport in [25, 465, 587]:
                return "Communication"

            # FTP
            elif dport in [20, 21]:
                return "Communication"

            # UDP voice/video traffic
            elif protocol == "UDP" and size > 1000:
                return "Communication"

            # Large TCP packets
            elif protocol == "TCP" and size > 1200:
                return "Communication"

            # Medium TCP packets
            elif protocol == "TCP" and size > 300:
                return "Browsing"

            # Small UDP packets
            elif protocol == "UDP" and size < 250:
                return "System"

            else:
                return "Unknown"

        df["traffic_type"] = df.apply(classify, axis=1)

        # ----------------------------------------
        # 6. Privacy Score
        # ----------------------------------------

        def privacy(row):

            score = 40

            if row["is_https"]:
                score += 25

            if row["protocol"] == "TCP":
                score += 10

            if row["packet_size"] < 600:
                score += 10

            if row["traffic_type"] == "System":
                score += 5

            return min(score, 100)

        df["privacy_score"] = df.apply(privacy, axis=1)

        # ----------------------------------------
        # 7. Traffic in MB
        # ----------------------------------------

        df["traffic_mb"] = (
            df["packet_size"] / (1024 * 1024)
        )

        # ----------------------------------------
        # 8. Carbon Estimate
        # ----------------------------------------

        CARBON_FACTOR = 0.06

        df["carbon_estimate"] = (
            df["traffic_mb"] * CARBON_FACTOR
        )

        # ----------------------------------------
        # 9. Packet Size Category
        # ----------------------------------------

        def packet_category(size):

            if size < 300:
                return "Small"

            elif size < 900:
                return "Medium"

            else:
                return "Large"

        df["packet_category"] = df["packet_size"].apply(packet_category)

        return df