import paramiko
import getpass
from datetime import datetime

def get_connection_details():
    """
    Prompt the user for the Windows machine's connection details.
    """
    ip_address = input("Enter the IP address of the Windows machine: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    return ip_address, username, password

def execute_command(ssh_client, command):
    """
    Execute a command on the remote SSH server and return the output.
    """
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode('utf-8').strip(), stderr.read().decode('utf-8').strip()

def run_updates(ip_address, username, password):
    """
    Connect to the Windows machine via SSH and run updates.
    """
    result = []

    try:
        # Create SSH client and connect
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_address, port=22, username=username, password=password)
        
        result.append("Connected to Windows machine successfully.\n")

        # Run Windows Update commands
        command = "powershell -Command \"Get-WindowsUpdate\""
        result.append("Checking for updates...\n")
        stdout, stderr = execute_command(ssh_client, command)
        result.append("Update Check Output:\n" + stdout + "\n")
        if stderr:
            result.append("Update Check Errors:\n" + stderr + "\n")

        command = "powershell -Command \"Install-WindowsUpdate -AcceptAll -AutoReboot\""
        result.append("Installing updates...\n")
        stdout, stderr = execute_command(ssh_client, command)
        result.append("Update Installation Output:\n" + stdout + "\n")
        if stderr:
            result.append("Update Installation Errors:\n" + stderr + "\n")

        result.append("Update process completed.\n")

    except Exception as e:
        result.append(f"Error: {e}\n")
    finally:
        ssh_client.close()

    return result

def write_results_to_file(results, ip_address):
    """
    Write the results to a text file with date and IP address.
    """
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"update_results_{ip_address.replace('.', '_')}_{date_str}.txt"
    with open(filename, "w") as file:
        file.writelines(results)
    print(f"Results have been written to {filename}")

def main():
    ip_address, username, password = get_connection_details()
    results = run_updates(ip_address, username, password)
    write_results_to_file(results, ip_address)

if __name__ == "__main__":
    main()
