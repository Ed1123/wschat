# Echo server program
import socket

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
MESSAGE_LENGTH = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f'Listening on {HOST}:{PORT}')

        clients = {}
        for i in range(2):
            conn, addr = server.accept()
            print(f'{addr} connected to server')
            clients[addr] = conn

        with list(clients.values())[0] as conn1, list(clients.values())[1] as conn2:
            while True:
                message = conn1.recv(MESSAGE_LENGTH).decode()
                print(f'1 sent: {message}')
                message = conn2.recv(MESSAGE_LENGTH).decode()
                print(f'2 sent: {message}')
                # if message == 'exit':
                # print(f'{addr} disconnected from server')
                # break


if __name__ == '__main__':
    main()
