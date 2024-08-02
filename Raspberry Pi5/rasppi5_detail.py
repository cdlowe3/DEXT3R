import paramiko
import re

# Configuration for SSH connection
HOST = '192.168.68.74'  # Replace with your Raspberry Pi's hostname or IP address
PORT = 22
USERNAME = 'cdlowe3'  # Replace with your Raspberry Pi's username
PASSWORD = 'cosadmin'  # Replace with your Raspberry Pi's password

def execute_command(ssh_client, command):
    """
    Execute a command on the remote SSH server and return the output.
    """
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode('utf-8').strip()

def get_system_info(ssh_client):
    """
    Retrieve OS information.
    """
    os_info = {}
    try:
        os_info['OS'] = execute_command(ssh_client, "uname -o")
        os_info['Kernel Version'] = execute_command(ssh_client, "uname -r")
        os_info['Architecture'] = execute_command(ssh_client, "uname -m")
        
        lsb_release_info = execute_command(ssh_client, "lsb_release -a")
        for line in lsb_release_info.splitlines():
            if "Distributor ID:" in line:
                os_info['Distributor'] = line.split(":")[1].strip()
            elif "Release:" in line:
                os_info['Release'] = line.split(":")[1].strip()
            elif "Codename:" in line:
                os_info['Codename'] = line.split(":")[1].strip()
    except Exception as e:
        print(f"Error retrieving OS information: {e}")
    
    return os_info

def get_cpu_info(ssh_client):
    """
    Retrieve CPU information.
    """
    cpu_info = {}
    try:
        cpu_info['CPU Model'] = execute_command(ssh_client, "cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2").strip()
        cpu_info['CPU Cores'] = execute_command(ssh_client, "nproc")
        cpu_info['CPU Frequency'] = execute_command(ssh_client, "vcgencmd measure_clock arm | cut -d= -f2") + " Hz"
    except Exception as e:
        print(f"Error retrieving CPU information: {e}")
    
    return cpu_info

def get_memory_info(ssh_client):
    """
    Retrieve memory information.
    """
    memory_info = {}
    try:
        mem_info = execute_command(ssh_client, "free -h")
        mem_info_lines = mem_info.splitlines()
        memory_info['Total RAM'] = mem_info_lines[1].split()[1]
        memory_info['Available RAM'] = mem_info_lines[1].split()[6]
        memory_info['Total Swap'] = mem_info_lines[2].split()[1]
        memory_info['Available Swap'] = mem_info_lines[2].split()[3]
    except Exception as e:
        print(f"Error retrieving memory information: {e}")
    
    return memory_info

def get_disk_info(ssh_client):
    """
    Retrieve disk usage information.
    """
    disk_info = {}
    try:
        disk_usage = execute_command(ssh_client, "df -h")
        disk_info['Disk Usage'] = disk_usage
    except Exception as e:
        print(f"Error retrieving disk usage: {e}")
    
    return disk_info

def print_system_info(ssh_client):
    """
    Print system information in a neofetch-like format.
    """
    os_info = get_system_info(ssh_client)
    cpu_info = get_cpu_info(ssh_client)
    memory_info = get_memory_info(ssh_client)
    disk_info = get_disk_info(ssh_client)

    print(f"```\n"
          f"       .-/+oossssoo+/-.   \n"
          f"      `:+sssssssssssssssy+   \n"
          f"    -+ssssssssssssssssss- \n"
          f"   :ssssssssssssssssss: \n"
          f"  :ssssssssssssssssss: \n"
          f"  :ssssssssssssssssss: \n"
          f"  :ssssssssssssssssss: \n"
          f"  :ssssssssssssssssss: \n"
          f"   :ssssssssssssssssss: \n"
          f"    -+ssssssssssssssssss- \n"
          f"      `:+sssssssssssssssy+ \n"
          f"       .-/+oossssoo+/-.\n\n"
          f"OS: {os_info.get('OS', 'N/A')} {os_info.get('Release', 'N/A')} ({os_info.get('Codename', 'N/A')})\n"
          f"Distributor: {os_info.get('Distributor', 'N/A')}\n"
          f"Kernel Version: {os_info.get('Kernel Version', 'N/A')}\n"
          f"Architecture: {os_info.get('Architecture', 'N/A')}\n"
          f"CPU Model: {cpu_info.get('CPU Model', 'N/A')}\n"
          f"CPU Cores: {cpu_info.get('CPU Cores', 'N/A')}\n"
          f"CPU Frequency: {cpu_info.get('CPU Frequency', 'N/A')}\n"
          f"RAM: {memory_info.get('Total RAM', 'N/A')} total, {memory_info.get('Available RAM', 'N/A')} available\n"
          f"Swap: {memory_info.get('Total Swap', 'N/A')} total, {memory_info.get('Available Swap', 'N/A')} available\n"
          f"Disk Usage:\n{disk_info.get('Disk Usage', 'N/A')}\n"
          f"```")

def main():
    try:
        # Create SSH client and connect
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD)

        print_system_info(ssh_client)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh_client.close()

if __name__ == "__main__":
    main()
