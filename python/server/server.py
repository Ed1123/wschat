# Echo server program
import socket

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
MESSAGE_LENGTH = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        conn, addr = server.accept()
        with conn:
            print('Connected by', addr)
            while True:
                message = conn.recv(MESSAGE_LENGTH).decode()
                print(message)
                if message == 'exit':
                    break


if __name__ == '__main__':
    main()
