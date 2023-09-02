# Importing the necessary libraries
import socket

# Connecting to UDP server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12000)

# Sending the message to the server
message = input("Enter a message to send: ")
client_socket.sendto(message.encode(), server_address)

# Receiving the response from the server
response, _ = client_socket.recvfrom(2048)
print(f"Received response: {response.decode()}")

# Closing the connection
client_socket.close()
