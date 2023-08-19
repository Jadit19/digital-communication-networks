import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12000)

message = input("Enter a message to send: ")
client_socket.sendto(message.encode(), server_address)    

response, _ = client_socket.recvfrom(2048)
print(f"Received response: {response.decode()}")

client_socket.close()
