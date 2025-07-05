import scapy.all as scapy
import logging

# Set up logging to capture suspicious activities
logging.basicConfig(filename="netguard.log", level=logging.INFO)

def packet_callback(packet):
    # Check if packet has an IP layer
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"Source: {ip_src} -> Destination: {ip_dst}")
        
        # Example anomaly: Unusual destination of the IP (outside any private IP range)
        if not ip_dst.startswith("192.168"):
            logging.warning(f"Suspicious Packet: Source: {ip_src}, Destination: {ip_dst}")
            print(f"Suspicious packet detected: {ip_src} -> {ip_dst}")

# Start sniffing on the default interface
scapy.sniff(prn=packet_callback, store=0)
