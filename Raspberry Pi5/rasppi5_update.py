### Writer - cdlowe3
### Date - July 31, 2024
### Reason - Remotely update Raspberry Pi5 - Only tested on Raspberry Pi5


import paramiko
import getpass

def get_connection_details():
    """
    Prompt the user for the Raspberry Pi's connection details.
    """
    ip_address = input("Enter the IP address of the Raspberry Pi: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    return ip_address, username, password

def execute_command(ssh_client, command):
    """
    Execute a command on the remote SSH server and return the output.
    """
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode('utf-8').strip()

def update_raspberry_pi(ip_address, username, password):
    """
    Connect to the Raspberry Pi and perform a system update.
    """
    try:
        # Create SSH client and connect
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_address, port=22, username=username, password=password)
        
        print("Connected to Raspberry Pi. Starting system update...")

        # Update package lists
        print("Updating package lists...")
        output = execute_command(ssh_client, "sudo apt full-upgrade")
        print(output)

        # Upgrade packages
        print("Upgrading packages...")
        output = execute_command(ssh_client, "sudo apt full-upgrade -y")
        print(output)

        print("System update completed.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh_client.close()

def main():
    ip_address, username, password = get_connection_details()
    update_raspberry_pi(ip_address, username, password)

if __name__ == "__main__":
    main()
