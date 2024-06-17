from vidstream import ScreenShareClient
import threading

# Define the IP address and port for the server
IP_ADDRESS = '127.0.0.1'
PORT = 4444

# Initialize the ScreenShareClient
sender = ScreenShareClient(IP_ADDRESS, PORT)

def start_stream():
    """
    Start the screen sharing stream.
    """
    try:
        sender.start_stream()
    except Exception as e:
        print(f"Error starting stream: {e}")

# Create and start a new thread to run the stream
t = threading.Thread(target=start_stream)
t.start()

try:
    # Wait for user input to stop the stream
    while input('Type "stop" to stop the screen sharing: ') != 'stop':
        continue
finally:
    # Stop the stream and join the thread
    sender.stop_stream()  # Use `stop_stream()` for client, not `stop_server()`
    t.join()
    print("Screen sharing has been stopped.")
