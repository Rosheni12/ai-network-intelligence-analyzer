print("Start")

from scapy.all import sniff

print("Scapy Imported")

packets = sniff(count=5)

print("Finished Sniffing")
print(len(packets))