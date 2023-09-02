# Importing the necessary libraries
import socket
import fcntl
import struct
import threading
import netifaces


# Making a Server class
class Server:
    # Constructor initialization, requires a port number as an input
    def __init__(self, port: int = 12000):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.get_local_ip()

    # Function to get the local IP address of the system where the server is running
    def get_local_ip(self):
        try:
            interfaces = netifaces.interfaces()
            ifname = ""
            for interface in interfaces:
                if interface[0] == "w":
                    ifname = interface
                    break
            self.ip_address = socket.inet_ntoa(
                fcntl.ioctl(
                    self.socket.fileno(),
                    0x8915,
                    struct.pack("256s", ifname[:15].encode()),
                )[20:24]
            )
        except Exception as e:
            print(f"❌ {e}")
            exit(1)

    # Function to receive data from the mobile device and print it
    def receive(self):
        while True:
            data, client_address = self.socket.recvfrom(2048)
            print(" " * 40, end="\r")
            print(f"📢 {data.decode()}")
            print(f"🎤 ", end="", flush=True)

    # Function to send the input message to the mobile device
    def send(self):
        while True:
            message = input(f"🎤 ")
            self.socket.sendto(message.encode(), self.client)

    # Function that starts the server
    def start(self):
        self.socket.bind((self.ip_address, self.port))
        self.receive_thread = threading.Thread(target=self.receive)
        self.send_thread = threading.Thread(target=self.send)
        self.receive_thread.start()
        self.send_thread.start()

    # Function to let the server what the client's local IP address and port are
    def set_client(self, client_ip, client_port):
        self.client = (client_ip, int(client_port))

    # Function to print the server's local IP address and port details
    def print_details(self):
        print(f"✅ Server IP         : {self.ip_address}")
        print(f"✅ Server Port       : {self.port}")

    # Deconstructor
    def __del__(self):
        self.receive_thread.join()
        self.send_thread.join()
        self.socket.close()


# Main code
if __name__ == "__main__":
    server = Server()
    server.print_details()
    client_ip = input("📱 Enter Mobile IP   : ")
    client_port = input("📱 Enter Mobile Port : ")
    server.set_client(client_ip, client_port)
    server.start()
