import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12000)
server_socket.bind(server_address)

print("UDP server is listening...")

while True:
  data, client_address = server_socket.recvfrom(2048)
  server_socket.sendto(data.upper(), client_address)
