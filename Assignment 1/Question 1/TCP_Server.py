# Importing the necessary libraries
import socket

# Creating a TCP Server and binding it to port 12000 of the local machine
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12000)
server_socket.bind(server_address)

# Start listening for client connections
server_socket.listen(1)
print("TCP server is listening...")

while True:
    # Establish connection with client
    client_socket, client_address = server_socket.accept()

    while True:
        #  Get data from client
        data = client_socket.recv(2048)
        if not data:
            break

        # Send uppercase data to client
        client_socket.send(data.upper())

    # Close client connection once message is sent
    client_socket.close()
