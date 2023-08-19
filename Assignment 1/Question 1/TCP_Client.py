import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12000)
client_socket.connect(server_address)

message = input("Enter a message to send: ")  
client_socket.send(message.encode())
  
response = client_socket.recv(2048)
print(f"Received response: {response.decode()}")

client_socket.close()
