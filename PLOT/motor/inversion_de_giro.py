"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import pi
import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow
# pip install prototools
from prototools import timer

W = 2 * pi * 60
T = np.arange(0, 1.42*1/60, 1/6000)

ANTIHORARIO = len(T)
HORARIO = len(T)-1, 0, -1


@timer
def animate(xs):
    for i in xs:
        drawnow(lambda: make_fig(i))


def make_fig(i):
    circle = 1.5 * (np.cos(W * T) + 1j*np.sin(W * T))
    plt.plot(circle.real, circle.imag)
    plt.plot([0, a.real[i]], [0, a.imag[i]], 'k')
    plt.plot([0, b.real[i]], [0, b.imag[i]], 'b')
    plt.plot([0, c.real[i]], [0, c.imag[i]], 'm')
    plt.plot([0, s.real[i]], [0, s.imag[i]], 'r')


a = np.sin(W * T) * (np.cos(0) + 1j*np.sin(0))
b = np.sin(W * T - 2*pi/3) * (np.cos(2*pi/3) + 1j*np.sin(2*pi/3))
c = np.sin(W * T + 2*pi/3) * (np.cos(-2*pi/3) + 1j*np.sin(-2*pi/3))
s = a + b + c


if __name__ == '__main__':
    animate(range(ANTIHORARIO))
    animate(range(*HORARIO))