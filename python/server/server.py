import socket
import threading
from dataclasses import dataclass

HOST = ''
PORT = 50007
MESSAGE_LENGTH = 1024
EXIT_MESSAGE = 'exit'
TIMEOUT = 0.1


@dataclass
class Client:
    conn: socket.socket
    ip_addr: str
    port: int


def handle_new_clients(server: socket.socket, stop_event: threading.Event):
    while not stop_event.is_set():
        try:
            conn, addr = server.accept()
        except socket.timeout:
            continue
        client = Client(conn, addr[0], addr[1])
        print(f'{client.ip_addr}:{client.port} connected to server')
        threading.Thread(
            target=handle_client_messages, args=(client, stop_event)
        ).start()
    print('Closing server...')


def handle_client_messages(client: Client, stop_event: threading.Event):
    conn = client.conn
    conn.settimeout(TIMEOUT)
    message = ''
    while not stop_event.is_set() and message != EXIT_MESSAGE:
        try:
            message = conn.recv(MESSAGE_LENGTH).decode()
            print(f'{client.ip_addr}:{client.port} sent: {message}')
        except TimeoutError:
            pass
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    print(f'{client.ip_addr}:{client.port} disconnected from server')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.settimeout(TIMEOUT)
        server.listen()
        host, port = server.getsockname()
        print(f'Listening on {host}:{port}')

        stop_event = threading.Event()
        clients_thread = threading.Thread(
            target=handle_new_clients, args=(server, stop_event)
        )

        try:
            clients_thread.start()
            input('Press enter to close server\n')
        except KeyboardInterrupt:
            pass
        stop_event.set()
        server.close()
        clients_thread.join()


if __name__ == '__main__':
    main()
