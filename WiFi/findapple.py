import subprocess
import re
import platform

# List of known Apple MAC address prefixes
APPLE_MAC_PREFIXES = [
    "00:1C:B3", "00:1E:C2", "00:1F:5B", "00:1D:A1", "00:1F:5B", "00:1B:63",
    "00:1C:43", "00:1C:82", "00:1F:16", "00:1D:AA", "00:1E:67", "00:1D:43",
    "00:1E:0B", "00:1D:6A", "00:1C:BF", "00:1F:29", "00:1C:DE", "00:1F:9F"
]

def ping_sweep(network_prefix):
    """
    Perform a ping sweep on the network to discover live hosts.
    """
    live_hosts = []
    for i in range(1, 255):  # Assumes /24 subnet
        ip = f"{network_prefix}.{i}"
        response = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            live_hosts.append(ip)
    return live_hosts

def get_arp_table():
    """
    Get the ARP table from the system.
    """
    if platform.system() == "Windows":
        output = subprocess.check_output("arp -a", shell=True, text=True)
    else:
        output = subprocess.check_output("arp -n", shell=True, text=True)
    return output

def parse_arp_table(arp_output):
    """
    Parse the ARP table to extract IP and MAC addresses.
    """
    arp_entries = []
    for line in arp_output.splitlines():
        if platform.system() == "Windows":
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]{17})", line)
        else:
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]{17})", line)
        if match:
            arp_entries.append((match.group(1), match.group(2)))
    return arp_entries

def is_apple_device(mac_address):
    """
    Check if the MAC address belongs to an Apple device.
    """
    prefix = ':'.join(mac_address.split(':')[:3]).upper()
    return any(prefix.startswith(apple_prefix) for apple_prefix in APPLE_MAC_PREFIXES)

def main():
    network_prefix = "x.x.0.0/24"  # Replace with your local network range
    print("Scanning network for live hosts...")
    live_hosts = ping_sweep(network_prefix)

    if not live_hosts:
        print("No live hosts found.")
        return

    print("Fetching ARP table...")
    arp_output = get_arp_table()
    arp_entries = parse_arp_table(arp_output)

    apple_devices = []
    for ip, mac in arp_entries:
        if ip in live_hosts and is_apple_device(mac):
            apple_devices.append({
                "ip": ip,
                "mac": mac
            })

    if apple_devices:
        print("Apple iOS devices found:")
        for device in apple_devices:
            print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
    else:
        print("No Apple iOS devices found.")

if __name__ == "__main__":
    main()
