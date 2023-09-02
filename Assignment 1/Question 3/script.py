import base64
import socket
import ssl

class Gmail:
  def __init__(self):
    self.smtp_server = "smtp.gmail.com"
    self.smtp_port = 465
    self.first_recipient = ""
  
  def print_exception(self, e: Exception):
    print("[ERROR]")
    print("----------------------")
    print(e)
  
  def login(self, username: str, password: str):
    self.username = username
    self.encoded_username = base64.b64encode(username.encode()).decode()
    self.encoded_password = base64.b64encode(password.encode()).decode()
    self.setup_sockets()
    try:
      self.interact()
      self.interact("EHLO Adit")
      self.interact("STARTTLS")
      self.interact("AUTH LOGIN")
      self.interact(self.encoded_username)
      self.interact(self.encoded_password)
      self.interact(f"MAIL FROM:<{self.username}>")
    except Exception as e:
      self.print_exception(e)
    
  def interact(self, command: str = ""):
    if str != "":
      self.ssl_socket.send((command + "\r\n").encode())
    response = self.ssl_socket.recv(4096).decode()
    print("[RUNNING]:", command if command != "" else "Greeting")
    print("----------------------")
    print(response)
    print("")
  
  def setup_sockets(self):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.smtp_server, self.smtp_port))
    self.ssl_context = ssl.create_default_context()
    self.ssl_socket = self.ssl_context.wrap_socket(self.socket, server_hostname=self.smtp_server)
  
  def add_recipient(self, recipient: str):
    try:
      self.interact(f"RCPT TO:<{recipient}>")
      if self.first_recipient != "":
        self.first_recipient = recipient
    except Exception as e:
      self.print_exception(e)
  
  def send_email(self, subject: str, message: str, attachment_path: str):
    try:
      self.interact("DATA")
      
      self.ssl_socket.send(f"Subject: {subject}\r\n".encode())
      self.ssl_socket.send("MIME-Version: 1.0\r\n".encode())
      self.ssl_socket.send(f"From: {self.username}\r\n".encode())
      self.ssl_socket.send(f"To: {self.first_recipient}\r\n".encode())
      self.ssl_socket.send("Content-type: multipart/mixed; boundary=boundary123\r\n\r\n".encode())
      self.ssl_socket.send("--boundary123\r\n".encode())
      self.ssl_socket.send("Content-type: text/plain; charset=utf-8\r\n\r\n".encode())
      self.ssl_socket.send(message.replace("\n", "\r\n").encode())
      self.ssl_socket.send("\r\n--boundary123\r\n".encode())
      attachment_name = attachment_path.split("/")[-1]
      self.ssl_socket.send(f"Content-Disposition: attachment; filename={attachment_name}\r\n".encode())
      self.ssl_socket.send("Content-Type: text/plain; charset=utf-8\r\n".encode())
      self.ssl_socket.send("Content-Transfer-Encoding: base64\r\n\r\n".encode())
      with open(attachment_path, "rb") as file:
        attachment_data = base64.b64encode(file.read()).decode()
        self.ssl_socket.send(attachment_data.encode())
      self.ssl_socket.send("\r\n--boundary123--\r\n".encode())
      
      self.interact(".")
      self.interact("QUIT")
    except Exception as e:
      self.print_exception(e)
    self.ssl_socket.close()

if __name__ == "__main__":
  client = Gmail()
  client.login("emailID@gmail.com", "app_password")
  client.add_recipient("aditj20@iitk.ac.in")
  client.add_recipient("200038@iitk.ac.in")
  client.send_email("TEST", "Hello", "/path/to/file")