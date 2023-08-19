import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12000)
server_socket.bind(server_address)

server_socket.listen(1)
print("TCP server is listening...")

while True:
  client_socket, client_address = server_socket.accept()
    
  while True:
    data = client_socket.recv(2048)
    if not data:
      break
    client_socket.send(data.upper())
    
  client_socket.close()
