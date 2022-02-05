"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random
from flask import Flask, render_template
from string import ascii_letters, digits

app = Flask(__name__)
LONGITUD_MINIMA = 8


def generar_password(longitud: int = LONGITUD_MINIMA):
    """Genera un password aleatorio

    :param longitud: longitud del password
    :return: password aleatorio
    """
    return ''.join(random.choices(ascii_letters + digits, k=longitud))


@app.route('/')
def index():
    password = generar_password()
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run()