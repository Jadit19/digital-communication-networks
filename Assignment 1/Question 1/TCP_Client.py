# Importing the necessary libraries
import socket

# Connecting to TCP Server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12000)
client_socket.connect(server_address)

# Sending the message to the server
message = input("Enter a message to send: ")
client_socket.send(message.encode())

# Receiving the response from the server
response = client_socket.recv(2048)
print(f"Received response: {response.decode()}")

# Closing the connection
client_socket.close()
