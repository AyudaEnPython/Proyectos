"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os
from datetime import datetime
from typing import Tuple
# pip install prototools
from prototools import int_input, menu_input, EMAIL_REGEX
from prototools.colorize import cyan, red


class DniException(Exception):
    """Excepción para DNI"""
    ...


class EmailException(Exception):
    """Excepción para Email"""
    ...


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
                raise DniException(red("El DNI debe tener 8 caracteres"))
            if not dni.isdigit():
                raise DniException(red("El DNI debe contener solo números"))
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
                raise EmailException(red("El email no es válido"))
            return email
        except EmailException as e:
            print(e)
            continue


def datenow(s: str) -> str:
    return datetime.now().strftime(s)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def agregar_usuario(
    metodos: Tuple[str, str, str], costo: str,
) -> Tuple[str, str, str, int, str]:
    nombre = input(cyan("Ingrese su nombre y apellido: "))
    dni = validar_dni(cyan("Ingrese su DNI: "))
    email = validar_email(cyan("Ingrese su email: "))
    n = int_input(cyan("Ingrese el número de cartones que desea comprar: "))
    print(cyan("Costo Total:"), f"S/.{n*costo}")
    pago = menu_input(metodos, numbers=True)
    return nombre, dni, email, n, pago


def modificar_informacion():
    lugar = input(cyan("Información: "))
    fecha = input(cyan("Fecha: "))
    hora = input(cyan("Hora: "))
    costo = input(cyan("Costo S/.: "))
    return lugar, fecha, hora, costo
