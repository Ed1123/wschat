# Echo client program
import argparse
import socket
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, help='host to connect to')
parser.add_argument('--port', type=int, help='port to connect to')
args = parser.parse_args()

HOST = args.host or ''
PORT = args.port or 50007
# MESSAGE_LENGTH = 1024
TIMEOUT = 0.1


def handle_send_message(s: socket.socket, stop_event: threading.Event):
    while not stop_event.is_set():
        msg = input('message: ')
        s.sendall(msg.encode())
        if msg == 'exit':
            stop_event.set()
            s.close()


def handle_receive_message(s: socket.socket, stop_event: threading.Event):
    while not stop_event.is_set():
        try:
            message = s.recv(1024).decode()
        except socket.timeout:
            continue
        print(message)
        if message == 'Connection closed.':
            s.close()
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        print(f'Connecting to {HOST}:{PORT}')
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f'Could not connect to {HOST}:{PORT}')
        exit(1)
    print(f'Connected to {HOST}:{PORT}')
    s.settimeout(TIMEOUT)
    print('Press enter to send message to server')
    print('Type "exit" to disconnect from server')
    stop_event = threading.Event()
    send_thread = threading.Thread(target=handle_send_message, args=(s, stop_event))
    received_thread = threading.Thread(
        target=handle_receive_message, args=(s, stop_event)
    )
    send_thread.start()
    received_thread.start()
    send_thread.join()
    received_thread.join()
    print('Disconnected from server')
