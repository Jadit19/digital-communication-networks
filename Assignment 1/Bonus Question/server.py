import cv2
import socket
import pickle
import struct
import threading

class VideoServer:
  def __init__(self, port, max_connections):
    self.max_connections = max_connections
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = socket.gethostbyname(socket.gethostname())
    self.socket_address = (host_ip, port)
    self.server_socket.bind(self.socket_address)
    self.clients = []
  
  def new_clients(self):
    while True:
      client_socket, addr = self.server_socket.accept()
      print(f"✅ {addr[0]}:{addr[1]}")
      self.clients.append([client_socket, addr])
  
  def start(self):
    self.server_socket.listen(self.max_connections)
    print(f"📢 {self.socket_address[0]}:{self.socket_address[1]} [LISTENING]")
    self.accept_clients()
    self.start_transmitting()
  
  def accept_clients(self):
    self.client_thread = threading.Thread(target=self.new_clients)
    self.client_thread.start()
    
  def start_transmitting(self):
    self.cap = cv2.VideoCapture(0)
    while True:
      _, frame = self.cap.read()
      data = pickle.dumps(frame)
      message_size = struct.pack("L", len(data))
      for client, addr in self.clients:
        try:
          client.sendall(message_size + data)
        except (ConnectionResetError, BrokenPipeError):
          self.clients.remove([client, addr])
          print(f"❌ {addr[0]}:{addr[1]}")
  
  def __del__(self):
    self.cap.release()
    for client, addr in self.clients:
      client.close()
    self.server_socket.close()
    
if __name__ == "__main__":
  video_server = VideoServer(12000, 10)
  video_server.start()