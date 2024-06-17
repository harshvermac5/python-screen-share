# install vidstream using 'pip install vidstream'
# Import the necessary modules
from vidstream import StreamingServer
import threading

# Define the IP address and port for the server
IP_ADDRESS = '127.0.0.1'
PORT = 4444

# Initialize the StreamingServer
receiver = StreamingServer(IP_ADDRESS, PORT)

# Function to start the server
def start_server():
    receiver.start_server()

# Create and start a new thread to run the server
t = threading.Thread(target=start_server)
t.start()

# Keep the main thread running until 'stop' is input
try:
    while input('Type "stop" to stop the server: ') != 'stop':
        continue
finally:
    receiver.stop_server()
    t.join()
    print("Server has been stopped.")
