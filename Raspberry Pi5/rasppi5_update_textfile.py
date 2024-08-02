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
    return stdout.read().decode('utf-8').strip(), stderr.read().decode('utf-8').strip()

def update_raspberry_pi(ip_address, username, password):
    """
    Connect to the Raspberry Pi and perform a system update.
    """
    result = []

    try:
        # Create SSH client and connect
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_address, port=22, username=username, password=password)

        result.append("Connected to Raspberry Pi. Starting system update...\n")

        # Update package lists
        result.append("Updating package lists...\n")
        stdout, stderr = execute_command(ssh_client, "sudo apt full-upgrade")
        result.append("Update Output:\n" + stdout + "\n")
        if stderr:
            result.append("Update Errors:\n" + stderr + "\n")

        # Upgrade packages
        result.append("Upgrading packages...\n")
        stdout, stderr = execute_command(ssh_client, "sudo apt full-upgrade -y")
        result.append("Upgrade Output:\n" + stdout + "\n")
        if stderr:
            result.append("Upgrade Errors:\n" + stderr + "\n")

        result.append("System update completed.\n")

    except Exception as e:
        result.append(f"Error: {e}\n")
    finally:
        ssh_client.close()

    return result

def write_results_to_file(results, filename="update_results.txt"):
    """
    Write the results to a text file.
    """
    with open(filename, "w") as file:
        file.writelines(results)

def main():
    ip_address, username, password = get_connection_details()
    results = update_raspberry_pi(ip_address, username, password)
    write_results_to_file(results)
    print(f"Results have been written to update_results.txt")

if __name__ == "__main__":
    main()
