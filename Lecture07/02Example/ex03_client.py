import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("I am going to send Hello world!")
    input("Press enter to proceed")
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))