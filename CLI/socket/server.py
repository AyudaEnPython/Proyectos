"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import logging
import socket
import threading
from datetime import datetime

HOST, PORT = "127.0.0.1", 65432
DATE, TIME = "%Y-%m-%d", "%H:%M:%S"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_datetime(format_):
    return datetime.now().strftime(format_)


def handle_client(client_socket, client_address):
    logging.info("Handling connection from %s:%s", *client_address)
    with client_socket:
        try:
            while True:
                client_option = client_socket.recv(1024).decode('utf-8')
                response = {
                    "0": f"Current date: {get_datetime(DATE)}",
                    "1": f"Current time: {get_datetime(TIME)}",
                    "2": "Connection closed!",
                }.get(client_option, "Invalid option. Try again!")
                client_socket.send(response.encode('utf-8'))
                if client_option == '2':
                    break
        except Exception as e:
            logging.error(
                "An error ocurred while handling client %s:%s - %s",
                 *client_address, e,
            )
        finally:
            logging.info("Connection closed from %s:%s", *client_address)


def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        try:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((host, port))
            server.listen()
            logging.info(f"Server started on {host}:{port}")
            while True:
                client_socket, client_address = server.accept()
                logging.info(
                    "Accepted connection from %s:%s", *client_address,
                )
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.start()
        except Exception as e:
            logging.critical("Server error: %s", e)
        finally:
            logging.info("Server is shutting down.")


if __name__ == "__main__":
    run_server(HOST, PORT)
