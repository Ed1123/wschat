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

        conn, addr = server.accept()
        print(f'{addr} connected to server')

        with conn:
            while True:
                message = conn.recv(MESSAGE_LENGTH).decode()
                print(f'{addr} sent: {message}')
                if message == 'exit':
                    print(f'{addr} disconnected from server')
                    break


if __name__ == '__main__':
    main()
