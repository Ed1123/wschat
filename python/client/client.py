# Echo client program
import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, help='host to connect to')
parser.add_argument('--port', type=int, help='port to connect to')
args = parser.parse_args()

HOST = args.host or ''
PORT = args.port or 50007
# MESSAGE_LENGTH = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        print(f'Connecting to {HOST}:{PORT}')
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f'Could not connect to {HOST}:{PORT}')
        exit(1)
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
