import subprocess
import re

def get_wifi_profiles():
    """
    Get the list of all Wi-Fi profiles stored on the system.
    """
    try:
        # Run the netsh command to get Wi-Fi profiles
        result = subprocess.check_output('netsh wlan show profiles', shell=True, text=True)
        # Find all profile names using regex
        profiles = re.findall(r'All User Profile\s*:\s*(.*)', result)
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error getting Wi-Fi profiles: {e}")
        return []

def get_wifi_password(profile):
    """
    Get the password for a given Wi-Fi profile.
    """
    try:
        # Run the netsh command to get details of the profile
        result = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True, text=True)
        # Find the password using regex
        match = re.search(r'Key Content\s*:\s*(.*)', result)
        return match.group(1) if match else 'No password set'
    except subprocess.CalledProcessError as e:
        print(f"Error getting Wi-Fi password for profile {profile}: {e}")
        return 'Error retrieving password'

def main():
    profiles = get_wifi_profiles()
    if profiles:
        print("Found Wi-Fi profiles:")
        for profile in profiles:
            password = get_wifi_password(profile)
            print(f"Profile: {profile}")
            print(f"Password: {password}")
            print("-" * 40)
    else:
        print("No Wi-Fi profiles found.")

if __name__ == '__main__':
    main()
