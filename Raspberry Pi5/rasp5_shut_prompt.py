### Written - cdlowe3
### Date - July 31st, 2024
### Reason - Remotely shutdown a Raspberry Pi5 with prompt for IP ADDR, Username, & Password - Only tested with RaspPi5.

import paramiko
import getpass

def shutdown_raspberry_pi(ip, username, password):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        # Automatically add the server's host key (this might be insecure)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the Raspberry Pi
        ssh.connect(ip, username=username, password=password)
        
        # Execute the reboot command
        stdin, stdout, stderr = ssh.exec_command('sudo /sbin/shutdown')
        
        # Wait for the command to complete
        stdout.channel.recv_exit_status()
        
        # Print any errors
        error = stderr.read().decode()
        if error:
            print(f"Error: {error}")
        else:
            print("Shutdown command sent successfully.")

        # Close the connection
        ssh.close()
    
    except paramiko.AuthenticationException:
        print("Authentication failed. Check your username/password.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = input("Enter the IP address or hostname of the Raspberry Pi: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    
    shutdown_raspberry_pi(ip, username, password)