from scapy.all import sniff

print("Listening for 5 packets...")

packets = sniff(count=5)

print(f"Captured {len(packets)} packets")