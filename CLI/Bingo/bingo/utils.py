"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os
from datetime import datetime
from typing import Tuple
# pip install prototools
from prototools import int_input, menu_input, EMAIL_REGEX


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


def agregar_usuario(
    metodos: Tuple[str, str, str] , costo: str,
) -> Tuple[str, str, str, int, str]:
    nombre = input("Ingrese su nombre y apellido: ")
    dni = validar_dni("Ingrese su DNI: ")
    email = validar_email("Ingrese su email: ")
    n = int_input("Ingrese el número de cartones que desea comprar: ")
    print(f"Costo Total: S/.{n*costo}")
    pago = menu_input(metodos, numbers=True)
    return nombre, dni, email, n, pago


def modificar_informacion():
    lugar = input("Información: ")
    fecha = input("Fecha: ")
    hora = input("Hora: ")
    costo = input("Costo S/.: ")
    return lugar, fecha, hora, costo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')