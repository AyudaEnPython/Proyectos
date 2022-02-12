"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Frame, Label, Radiobutton, StringVar, Tk
from typing import Tuple

GRID_RADIOBUTTONS: Tuple[int, str, str] = (
    (0, "Sumar", "+"),
    (1, "Restar", "-"),
    (2, "Multiplicar", "*"),
    (3, "Dividir", "/"),
)
GRID_LABELS: Tuple[str, int, int] = (
    ("Primer número", 0, 0),
    ("Segundo número", 2, 0),
    ("Resultado", 4, 0),
)


def calcular(x: float, operador: str, y: float) -> float:
    """Calcula el resultado de una operación matemática

    :param x: primer número
    :type x: float
    :param operador: operador matemático
    :type operador: str
    :param y: segundo número
    :type y: float
    :return: resultado de la operación
    :rtype: float
    """
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y if y != 0 else "Error",
    }[operador]


class Calculadora(Frame):

    _i = 0

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculadora")
        self.widgets()
        self.layout()

    def widgets(self):
        self.frm_entries = Frame(self.root)
        self.frm_bottom = Frame(self.root)
        self.frm_operadores = Frame(self.root)
        self.a = Entry(self.frm_entries)
        self.b = Entry(self.frm_entries)
        self.c = Entry(self.frm_entries)
        self.btn_calcular = Button(
            self.frm_bottom, text="Calcular", command=self._f
        )
        self.btn_limpiar = Button(
            self.frm_bottom, text="Limpiar", command=self._clear
        )
        self.counter = Label(self.frm_bottom, text=f"Operaciones: {0}")
        self.operador = StringVar(value="+")
        for _, text, valor in GRID_RADIOBUTTONS:
            Radiobutton(
                self.frm_operadores, text=text, value=valor,
                variable=self.operador,
            ).grid(sticky="w")
        for text, row, col in GRID_LABELS:
            Label(self.frm_entries, text=text).grid(row=row, column=col)

    def layout(self):
        self.frm_entries.grid(row=0, column=0)
        self.frm_operadores.grid(row=0, column=1)
        self.frm_bottom.grid(row=1, columnspan=3)
        self.a.grid(row=1, column=0, padx=15, pady=5)
        self.b.grid(row=3, column=0, padx=15, pady=5)
        self.c.grid(row=5, column=0, padx=15, pady=5)
        self.btn_limpiar.grid(row=0, column=0, padx=15, pady=5)
        self.btn_calcular.grid(row=0, column=1, padx=5, pady=5)
        self.counter.grid(row=0, column=2, padx=15, pady=5)

    def _f(self):
        result = calcular(
            float(self.a.get()), self.operador.get(), float(self.b.get())
        )
        self.c.delete(0, "end")
        self.c.insert(0, f"{result:.2f}")
        __class__._i += 1
        self.counter.config(text=f"Operaciones: {__class__._i}")

    def _clear(self):
        for w in (self.a, self.b, self.c):
            w.delete(0, "end")

    def run(self):
        self.root.title("Ayuda En Python")
        self.root.geometry("260x195")
        self.root.mainloop()


if __name__ == "__main__":
    app = Calculadora()
    app.run()
