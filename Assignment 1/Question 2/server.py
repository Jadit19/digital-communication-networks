import socket
import fcntl
import struct
import threading
import netifaces

class Server:
  def __init__(self, port: int = 12000):
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.get_local_ip()
  
  def get_local_ip(self):
    try:
      interfaces = netifaces.interfaces()
      ifname = ""
      for interface in interfaces:
        if interface[0] == "w":
          ifname = interface
          break
      self.ip_address = socket.inet_ntoa(fcntl.ioctl(
        self.socket.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15].encode())
      )[20:24])
    except Exception as e:
      print(f"❌ {e}")
      exit(1)
  
  def receive(self):
    while True:
      data, client_address = self.socket.recvfrom(2048)
      print(" "*40, end="\r")
      print(f"📢 {data.decode()}")
      print(f"🎤 ", end="", flush=True)
  
  def send(self):
    while True:
      message = input(f"🎤 ")
      self.socket.sendto(message.encode(), self.client)
  
  def start(self):
    self.socket.bind((self.ip_address, self.port))
    self.receive_thread = threading.Thread(target=self.receive)
    self.send_thread = threading.Thread(target=self.send)
    self.receive_thread.start()
    self.send_thread.start()
    
  def set_client(self, client_ip, client_port):
    self.client = (client_ip, int(client_port))
  
  def print_details(self):
    print(f"✅ Server IP         : {self.ip_address}")
    print(f"✅ Server Port       : {self.port}")
  
  def __del__(self):
    self.receive_thread.join()
    self.send_thread.join()
    self.socket.close()

if __name__ == '__main__':
  server = Server()
  server.print_details()
  client_ip = input("📱 Enter Mobile IP   : ")
  client_port = input("📱 Enter Mobile Port : ")
  server.set_client(client_ip, client_port)
  server.start()