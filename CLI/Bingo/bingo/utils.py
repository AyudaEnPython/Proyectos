"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
from typing import Tuple
# pip install prototools
from prototools.inputs import int_input, menu_input

METODOS = ("VISA", "Transferencia BCP", "Yape")


def datenow(s: str) -> str:
    return datetime.now().strftime(s)


def agregar_usuario() -> Tuple[str, str, str, str]:
    nombre = input("Ingrese su nombre y apellido: ")
    dni = input("Ingrese su DNI: ")
    email = input("Ingrese su email: ")
    n = int_input("Ingrese el número de cartones que desea comprar: ")
    print(f"Costo Total: S/.{n*5}")
    pago = menu_input(METODOS, numbers=True)
    return nombre, dni, email, n, pago