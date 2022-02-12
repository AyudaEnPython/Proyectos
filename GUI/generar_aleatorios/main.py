"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from tkinter import Entry, Tk, Button, Label, Spinbox


def generar_aleatorio(minimo: int =0, maximo: int = 100) -> int:
    """Genera un número aleatorio entre dos valores dados

    :param minimo: valor mínimo
    :minimo type: int
    :param maximo: valor máximo
    :maximo type: int
    :return: número aleatorio entre los dos valores dados
    :rtype: int
    """
    if minimo > maximo:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo")
    return randint(minimo, maximo)


class Generador:

    def __init__(self) -> None:
        self.root = Tk()
        self.widgets()
        self.layout()
    
    def widgets(self):
        self.lbl_min = Label(self.root, text="Minimo")
        self.minimo = Spinbox(self.root, from_=0, to=100)
        self.lbl_max = Label(self.root, text="Maximo")
        self.maximo = Spinbox(self.root, from_=0, to=100)
        self.lbl_res = Label(self.root, text="Número generado")
        self.ent_res = Entry(self.root)
        self.clear = Button(self.root, text="Limpiar", command=self._clear)
        self.generar = Button(self.root, text="Generar", command=self._f)
    
    def _clear(self):
        self.ent_res.delete(0, "end")
        self._clear_spinbox()

    def _clear_spinbox(self):
        self.minimo.delete(0, "end")
        self.minimo.insert(0, 0)
        self.maximo.delete(0, "end")
        self.maximo.insert(0, 0)

    def _f(self):
        self.ent_res.delete(0, "end")
        minimo = int(self.minimo.get())
        maximo = int(self.maximo.get())
        try:
            resultado = generar_aleatorio(minimo, maximo)
        except ValueError as e:
            resultado = e
        self.ent_res.insert(0, resultado)

    def layout(self):
        self.lbl_min.grid(row=0, column=0, padx=5, pady=5)
        self.minimo.grid(row=0, column=1, padx=5, pady=5)
        self.lbl_max.grid(row=1, column=0, padx=5, pady=5)
        self.maximo.grid(row=1, column=1, padx=5, pady=5)
        self.lbl_res.grid(row=2, column=0, padx=5, pady=5)
        self.ent_res.grid(row=2, column=1, padx=5, pady=5)
        self.clear.grid(row=3, column=0, padx=5, pady=5)
        self.generar.grid(row=3, column=1, padx=5, pady=5)

    def run(self):
        self.title("Ayuda En Python")
        self.root.mainloop()


if __name__ == "__main__":
    app = Generador()
    app.run()
