import paramiko
import getpass
import datetime

def run_apt_update_remote(hostname, port, username, password):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        
        # Automatically add the remote host's key (for demo purposes)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote device
        ssh.connect(hostname, port=port, username=username, password=password)
        
        # Execute the 'sudo apt update' command
        stdin, stdout, stderr = ssh.exec_command('sudo apt update')
        
        # Send the password for sudo if required
        stdin.write(password + '\n')
        stdin.flush()
        
        # Read the command output and error
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        # Create a filename based on device name and date
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        filename = f"{hostname}_{date_str}_apt_update_output.txt"
        
        # Write the output to the file
        with open(filename, 'w') as file:
            file.write("Output of 'sudo apt update':\n")
            if output:
                file.write(output)
            if error:
                file.write("\nError output:\n")
                file.write(error)
        
        print(f"Output saved to {filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Prompt for user input
    hostname = input("Enter the IP address or hostname of the remote device: ")
    port = 22  # Default SSH port
    username = input("Enter your SSH username: ")
    password = getpass.getpass("Enter your SSH password: ")
    
    run_apt_update_remote(hostname, port, username, password)
