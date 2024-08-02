import subprocess
import re

def get_available_networks():
    """
    Use netsh to get available wireless networks.
    """
    try:
        # Run the netsh command to get the list of available wireless networks
        result = subprocess.check_output('netsh wlan show networks', shell=True, text=True)
        # Find all network names using regex
        networks = re.findall(r'SSID\s*\d+\s*:\s*(.*)', result)
        return networks
    except subprocess.CalledProcessError as e:
        print(f"Error getting available networks: {e}")
        return []

def main():
    print("Scanning for available wireless networks...")
    networks = get_available_networks()
    if networks:
        print("Available Networks:")
        for network in networks:
            print(f"- {network}")
    else:
        print("No networks found.")

if __name__ == '__main__':
    main()
