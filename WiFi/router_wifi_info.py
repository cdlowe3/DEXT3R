import requests
from requests.auth import HTTPBasicAuth

def get_router_data(url, username, password):
    """
    Retrieve data from the router using HTTP GET request.
    """
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        return response.json()  # Assuming the router API returns JSON data
    except requests.RequestException as e:
        print(f"Error retrieving data from router: {e}")
        return None

def extract_wifi_info(data):
    """
    Extract Wi-Fi information from router data.
    """
    if not data:
        print("No data to extract information from.")
        return

    # Example extraction logic, modify based on actual data format
    networks = data.get('wireless_networks', [])
    for network in networks:
        ssid = network.get('SSID')
        password = network.get('password', 'No password set')
        print(f"Network SSID: {ssid}")
        print(f"Password: {password}")
        print("-" * 40)

def main():
    router_url = 'http://x.x.x.x/api/wifi'  # Replace with your router's API URL
    username = 'admin'  # Replace with your router's username
    password = 'admin'  # Replace with your router's password

    print("Retrieving wireless network information...")
    data = get_router_data(router_url, username, password)
    extract_wifi_info(data)

if __name__ == '__main__':
    main()
