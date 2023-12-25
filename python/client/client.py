# Echo client program
import socket

HOST = 'localhost'  # The remote host
PORT = 50007  # The same port as used by the server
# MESSAGE_LENGTH = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Connected to {HOST}:{PORT}')
    print('Press enter to send message to server')
    print('Type "exit" to disconnect from server')
    while True:
        msg = input('message: ')
        s.sendall(msg.encode())
        if msg == 'exit':
            s.close()
            print('Disconnected from server')
            break
        # data = s.recv(1024)
        # print('Received', repr(data))
