import socket
import threading
import requests

def scan_ip(ip):
    """
    Scan a single IP to check if the host is up.
    """
    try:
        # Ping the IP address (using socket timeout as a basic check)
        socket.create_connection((ip, 80), timeout=2).close()
        return ip
    except (socket.timeout, socket.error):
        return None

def scan_network(network_range):
    """
    Scan the network to find live hosts.
    """
    live_hosts = []
    threads = []
    
    for i in range(1, 255):  # Assuming /24 subnet, adjust as needed
        ip = f"{network_range}.{i}"
        thread = threading.Thread(target=lambda ip=ip: live_hosts.append(scan_ip(ip)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    live_hosts = [host for host in live_hosts if host is not None]
    print(f"Live hosts found: {live_hosts}")
    return live_hosts

def check_services(ip):
    """
    Check for HTTP and FTP services on the given IP.
    """
    try:
        # Check HTTP service
        try:
            response = requests.get(f'http://{ip}', timeout=3)
            print(f"HTTP Service on {ip}: {response.status_code}")
        except requests.RequestException:
            pass

        # Check FTP service
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, 21))
            banner = s.recv(1024).decode().strip()
            print(f"FTP Banner on {ip}: {banner}")
            s.close()
        except socket.error:
            pass

    except Exception as e:
        print(f"Error checking services on {ip}: {e}")

def main():
    network_range = '192.168'  # Replace with your local network base address
    print("Scanning network...")
    live_hosts = scan_network(network_range)
    
    if live_hosts:
        print("Checking services on live hosts...")
        for host in live_hosts:
            check_services(host)
    else:
        print("No live hosts found.")

if __name__ == '__main__':
    main()
