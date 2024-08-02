import nmap
import socket
import requests

def scan_network(network_range):
    """
    Scan the network to find live hosts and their open ports.
    """
    nm = nmap.PortScanner()
    print(f"Scanning network range: {network_range}")
    nm.scan(hosts=network_range, arguments='-p 1-1024')  # Scan common ports

    hosts = nm.all_hosts()
    print(f"Found hosts: {hosts}")

    return nm

def check_services(nm, hosts):
    """
    Check for services running on the detected hosts.
    """
    for host in hosts:
        print(f"Checking services on {host}...")
        try:
            # Try to fetch the banner on HTTP port 80
            if '80/tcp' in nm[host]['tcp']:
                try:
                    response = requests.get(f'http://{host}', timeout=3)
                    print(f"HTTP Service on {host}: {response.status_code}")
                except requests.RequestException as e:
                    print(f"Error accessing HTTP service on {host}: {e}")
                
            # Try to fetch the banner on FTP port 21
            if '21/tcp' in nm[host]['tcp']:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(3)
                    s.connect((host, 21))
                    banner = s.recv(1024).decode()
                    print(f"FTP Banner on {host}: {banner.strip()}")
                    s.close()
                except socket.error as e:
                    print(f"Error accessing FTP service on {host}: {e}")

        except Exception as e:
            print(f"Error checking services on {host}: {e}")

def main():
    network_range = '192.168.1.0/24'  # Replace with your local network range
    nm = scan_network(network_range)
    hosts = nm.all_hosts()
    if hosts:
        check_services(nm, hosts)
    else:
        print("No hosts found.")

if __name__ == '__main__':
    main()
