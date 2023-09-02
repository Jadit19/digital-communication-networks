# Importing the necessary libraries
import cv2
import socket
import pickle
import struct


# Making a VideoClient class
class VideoClient:
    # Constructor initilization, requires server IP address and port number
    def __init__(self, host_ip, host_port):
        self.socket_addr = (host_ip, host_port)
        self.make_connection()

    # Function to establish connection to server
    def make_connection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.socket_addr)

    # Function to start accepting data from server and display it
    def start(self):
        data = b""
        payload_size = struct.calcsize("L")
        while True:
            while len(data) < payload_size:
                data += self.client_socket.recv(2048)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.client_socket.recv(2048)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("Live Stream", frame)
            cv2.waitKey(1)

    # Deconstructor, closes the socket
    def __del__(self):
        self.client_socket.close()


if __name__ == "__main__":
    video_client = VideoClient("127.0.1.1", 12000)
    video_client.start()
