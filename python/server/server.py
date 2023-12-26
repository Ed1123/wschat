import socket
import threading
from dataclasses import dataclass

HOST = 'localhost'
PORT = 50007
MESSAGE_LENGTH = 1024
EXIT_MESSAGE = 'exit'


@dataclass
class Client:
    conn: socket.socket
    ip_addr: str
    port: int


def handle_new_clients(server: socket.socket, stop_event: threading.Event):
    try:
        while not stop_event.is_set():
            conn, addr = server.accept()
            client = Client(conn, addr[0], addr[1])
            print(f'{client.ip_addr}:{client.port} connected to server')
            threading.Thread(target=handle_client_messages, args=(client,)).start()
    except ConnectionAbortedError:
        print('Closing server...')


def handle_client_messages(client: Client):
    with client.conn as conn:
        while True:
            message = conn.recv(MESSAGE_LENGTH).decode()
            print(f'{client.ip_addr}:{client.port} sent: {message}')
            if message == 'exit':
                print(f'{client.ip_addr}:{client.port} disconnected from server')
                break


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f'Listening on {HOST}:{PORT}')

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
