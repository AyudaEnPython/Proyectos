"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
from typing import Tuple
# pip install prototools
from prototools import int_input, menu_input, EMAIL_REGEX
from . import PRECIO, METODOS


class DniException(Exception):
    """Excepción para DNI"""
    ...


class EmailException(Exception):
    """Excepción para Email"""
    ...


def datenow(s: str) -> str:
    return datetime.now().strftime(s)


# Adaptado de:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/persona_dni.py
def validar_dni(s: str) -> str:
    """Valida un DNI

    :param s: Mensaje de indicación
    :type s: str
    :return: DNI validado
    :rtype: str
    """
    while True:
        try:
            dni = input(s)
            if len(dni) != 8:
                raise DniException("El DNI debe tener 8 caracteres")
            if not dni.isdigit():
                raise DniException("El DNI debe contener solo números")
            return dni
        except DniException as e:
            print(e)
            continue


def validar_email(s: str) -> str:
    """Valida un email

    :param s: Mensaje de indicación
    :type s: str
    :return: Email validado
    :rtype: str
    """
    while True:
        try:
            email = input(s)
            if not EMAIL_REGEX.match(email):
                raise EmailException("El email no es válido")
            return email
        except EmailException as e:
            print(e)
            continue


def agregar_usuario() -> Tuple[str, str, str, int, str]:
    nombre = input("Ingrese su nombre y apellido: ")
    dni = validar_dni("Ingrese su DNI: ")
    email = validar_email("Ingrese su email: ")
    n = int_input("Ingrese el número de cartones que desea comprar: ")
    print(f"Costo Total: S/.{n*PRECIO}")
    pago = menu_input(METODOS, numbers=True)
    return nombre, dni, email, n, pago