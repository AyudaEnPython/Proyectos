"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List
from random import sample, shuffle
# pip install prototools
from prototools import tabulate, textbox
from prototools.colorize import cyan, green, red, yellow

from . import RANGOS, INDEX
from .models import Usuario, Numero
from .utils import clear


class Carton:
    _id: int = 0
    
    def __init__(self) -> None:
        self.posiciones = {}
        self.bingo = {"row": [0]*5, "col": [0]*5, "diagonal": [0]*2}
        self._create()

    def n_serial(self):
        return f"Número de serie: {self.serial:03d}"

    def _create(self) -> None:
        self.__class__._id += 1
        self.serial = self._id
        carton = [[0]*5 for _ in range(5)]
        for i in range(5):
            sample_ = sample(range(*RANGOS[i]), 5)
            for j in range(5):
                n = Numero(sample_.pop())
                carton[i][j] = n
                self.posiciones[n.valor] = (i, j)
        carton[2][2] = yellow(" "+ chr(9788)+" ")
        self.carton = list(map(list, zip(*carton)))

    def update(self, numero: int) -> None:
        if numero in self.posiciones:
            j, i = self.posiciones[numero]
            if i == j == 2:
                pass
            else:
                self.carton[i][j].marcar()
                self._update(i, j)

    def _update(self, i: int, j: int) -> None:
        self.bingo["row"][i] += 1
        self.bingo["col"][j] += 1
        if i == j == 2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif i == j:
            self.bingo["diagonal"][0] += 1
        elif i + j == 4:
            self.bingo["diagonal"][1] += 1

    def check(self) -> bool:
        return (
            5 in self.bingo["row"] or
            5 in self.bingo["col"] or
            4 in self.bingo["diagonal"]
        )

    def reset(self) -> None:
        self.bingo = {"row": [0]*5, "col": [0]*5, "diagonal": [0]*2}
        for i, j in self.posiciones.values():
            if i == j == 2:
                continue
            self.carton[i][j].desmarcar()

    def show(self) -> str:
        carton = tabulate(
            self.carton,
            align="center",
            inner=True,
            headers=[e for e in "BINGO"],
            border_type="double",
            color=cyan,
        )
        return f"\n{self.n_serial()}\n{carton}\n"

    def __repr__(self) -> str:
        return f"{self.serial:03d}"


@dataclass
class Game:
    usuarios: List[Usuario] = field(default_factory=list)
    numeros: List[int] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        self.stop = False
        self._generar_numeros()
        self._tablero()

    def add_user(self, args) -> None:
        usuario = Usuario(*args)
        for _ in range(usuario.n):
            usuario.add(Carton())
        self.usuarios.append(usuario)

    def _generar_numeros(self) -> None:
        self.numeros = list(range(1, 76))
        shuffle(self.numeros)

    def _tablero(self) -> None:
        self.numeros_jugados = [["--"]*16 for _ in range(5)]
        for i, letter in zip(range(5), "BINGO"):
            self.numeros_jugados[i][0] = letter

    def _sacar_numero(self) -> int:
        return self.numeros.pop()

    def play(self) -> None:
        clear()
        numero: int = self._sacar_numero()
        index, t = INDEX[numero]
        self.numeros_jugados[index][numero + t] = f"{numero:02d}"
        self.show()
        for usuario in self.usuarios:
            usuario.update(numero)
            usuario.show()
            if usuario.check():
                textbox(green(f"{usuario.nombre} gana!"), bcolor="green")
                self.winner = usuario
                self.stop = True

    def start(self) -> None:
        while not self.stop:
            self.play()
            _ = input("Presione ENTER para mostrar el siguiente número...")
        print(f"El ganador es {self.winner.nombre}")
        self.reset()

    def reset(self) -> None:
        self.stop = False
        self._generar_numeros()
        self._tablero()
        for usuario in self.usuarios:
            usuario.reset()

    def show(self) -> None:
        board = tabulate(
            self.numeros_jugados,
            headless=True,
            inner=True,
            color=red,
        )
        print(board)