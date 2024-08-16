"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import socket
# pip install prototools
from prototools import menu_input, textbox

MENU = "View current date", "View current time", "Exit"


def run_client(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_ip, server_port))
        while True:
            selected_option = menu_input(MENU, numbers=True)
            option = str(MENU.index(selected_option))
            client.send(option.encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            textbox(response, bcolor="cyan")
            if option == "2":
                break


if __name__ == "__main__":
    run_client("127.0.0.1", 65432)
