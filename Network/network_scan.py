import socket
import subprocess
import platform
import ipaddress
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_ip(ip):
    """
    Ping an IP address to check if it's active.
    """
    # Determine the command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', str(ip)]
    
    # Execute the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Check if the ping was successful
    return ip if result.returncode == 0 else None

def scan_network(network):
    """
    Scan all IP addresses in the given network range.
    """
    active_ips = []
    # Create a ThreadPoolExecutor to speed up the scanning process
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(ping_ip, ip) for ip in network.hosts()]
        for future in as_completed(futures):
            result = future.result()
            if result:
                active_ips.append(result)
    
    return active_ips

def print_devices(devices):
    """
    Print the discovered devices.
    """
    print("Active devices on the network:")
    print("IP Address")
    print("------------------------")
    for device in devices:
        print(device)

if __name__ == '__main__':
    # Define the network range to scan (e.g., 192.168.68.0/24)
    network_range = '192.168.68.0/24'
    network = ipaddress.ip_network(network_range)
    
    print(f"Scanning network range: {network_range}")
    
    active_ips = scan_network(network)
    print_devices(active_ips)
