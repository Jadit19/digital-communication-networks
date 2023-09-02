# Importing the necessary libraries
import socket

# Creating a TCP Server and binding it to port 12000 of the local machine
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12000)
server_socket.bind(server_address)

print("UDP server is listening...")

while True:
    # Establish connection with client
    data, client_address = server_socket.recvfrom(2048)

    # Send uppercase data to client
    server_socket.sendto(data.upper(), client_address)
