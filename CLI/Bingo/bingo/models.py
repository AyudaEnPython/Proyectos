"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List, Type
# pip install prototools
from prototools.colorize import red
from .utils import datenow

@dataclass
class Usuario:
    nombre: str
    dni: str
    email: str
    n: int
    pago: str
    fecha: str = field(default_factory=lambda: datenow("%d/%m/%Y"))
    hora: str = field(default_factory=lambda: datenow("%H:%M"))
    cartones: List[Type[object]] = field(default_factory=list)

    def add(self, carton: object) -> None:
        self.cartones.append(carton)

    def update(self, numero: int) -> None:
        for carton in self.cartones:
            carton.update(numero)
    
    def check(self) -> bool:
        for carton in self.cartones:
            if carton.check():
                return True
        return False

    def reset(self) -> None:
        for carton in self.cartones:
            carton.reset()

    def show(self) -> None:
        for carton in self.cartones:
            print(carton.show())

    def __str__(self) -> str:
        return f"{self.nombre} | {self.dni} | {self.email}"


@dataclass(order=True)
class Numero:
    _valor: int
    _marcado: bool = False

    @property
    def valor(self) -> int:
        return self._valor

    @property
    def marcado(self) -> bool:
        return self._marcado

    def marcar(self) -> None:
        self._marcado = True
    
    def desmarcar(self) -> None:
        self._marcado = False

    def __format__(self, _fmt) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        s = red(" *") if self._marcado else "  "
        return f"{self.valor:02d}{s}"