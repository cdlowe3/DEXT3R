### Writer: cdlowe3
### Date: July 31st 2024
### Reason: Remotely shutdown Raspberry Pi5 - Have not tested with previous Raspberry Pi's


import paramiko
import getpass

# Configuration
hostname = '192.168.68.74'  # Replace with your Raspberry Pi's hostname or IP address
port = 22                       # Default SSH port
username = 'cdlowe3'                 # Replace with your Raspberry Pi username
password = None                 # If you use key-based authentication, leave this as None

# Prompt for usernmae if not using key-based authentication
#if username is None:
#    username = getpass.username(prompt='Enter SSH username: ')

if password is None:
    password = getpass.getpass(prompt='Enter SSH password: ')

def reboot_raspberry_pi(hostname, port, username, password):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the Raspberry Pi
        ssh.connect(hostname, port, username, password)
        
        # Execute the shutdown command
        stdin, stdout, stderr = ssh.exec_command('sudo reboot -h now')
        stdout.channel.recv_exit_status()  # Wait for the command to complete
        
        # Print output and error (if any)
        print("STDOUT:", stdout.read().decode())
        print("STDERR:", stderr.read().decode())
        
        # Close the SSH connection
        ssh.close()
        print("Reboot command sent successfully.")
        
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    reboot_raspberry_pi(hostname, port, username, password)
