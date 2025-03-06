from scapy.all import ARP, Ether, srp
import ARP 
import Ether
import srp
import socket
import requests

def get_local_ip():
    """Get the local IP address of the current machine."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

def get_mac_vendor(mac_address):
    """Fetch vendor name using an online API (https://macvendors.com)."""
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except Exception:
        pass
    return "Unknown Vendor"

def scan_network(ip_range):
    """Scan the local network and return connected devices."""
    print(f"Scanning network: {ip_range}...")
    
    # Create ARP request
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast
    packet = ether / arp_request

    # Send packet and receive responses
    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        mac_vendor = get_mac_vendor(received.hwsrc)
        devices.append({
            "IP Address": received.psrc,
            "MAC Address": received.hwsrc,
            "Vendor": mac_vendor
        })
    
    return devices

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        network_prefix = ".".join(local_ip.split(".")[:-1]) + ".1/24"  # Scans the entire subnet (e.g., 192.168.1.1/24)
        devices = scan_network(network_prefix)

        if devices:
            print("\n📡 Connected Devices:")
            print("-" * 50)
            for device in devices:
                print(f"IP Address: {device['IP Address']}")
                print(f"MAC Address: {device['MAC Address']}")
                print(f"Vendor: {device['Vendor']}")
                print("-" * 50)
        else:
            print("No devices found.")