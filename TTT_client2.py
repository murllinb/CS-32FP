import os
import sys
import threading

from socket32 import create_new_socket
# Connect to server
# Display/recieve information from server
# Request user input for where they want to put there dice
# 

### Clear terminal logic that was in the original TTT code (GAI) for possible later implementation 
def clear():
    os.system("cls" if os.name == "nt" else "clear")


### Port priority logic that was remolded to allow the clients to determine which port they need to connects to for accesing the server
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

### Read server messaging ###
def server_message (conn, stop_event: threading.Event):
        while not stop_event.is_set():
            message = conn.recv()
            if not message:
                print("\n  [Disconnected from server]")
                stop_event.set()
                break
            print(message, end="", flush=True)

def main(): ### Bulk of logic here GAI helped write to define start and stop events with threading (especially daemon logic)
    with create_new_socket() as conn:
        try:
            conn.connect(HOST, PORT)
            print(f"  Connected to {HOST}:{PORT}\n")
        except ConnectionRefusedError:
            print(f"  Could not connect to {HOST}:{PORT}. Is the server running?")
            sys.exit(1)
 
        stop_event = threading.Event()

        recv_thread = threading.Thread(target=server_message, args=(conn, stop_event), daemon=True)
        recv_thread.start()

        try:
            while not stop_event.is_set():
                user_input = input()
                if stop_event.is_set():
                    break
                conn.sendall(user_input + "\n")
        except (KeyboardInterrupt, EOFError):
            print("\n  [Quit]")
 
 
if __name__ == "__main__":
    main()
