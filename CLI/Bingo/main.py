"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from typing import Tuple
from prototools import Menu
from prototools.colorize import magenta, cyan, yellow

from bingo.bingo import Game
from bingo.utils import agregar_usuario, modificar_informacion, datenow
from bingo import LUGAR, FECHA, HORA, COSTO, METODOS


class App:

    def __init__(self, lugar: str, fecha: str, hora: str, costo: str) -> None:
        self.game = Game()
        self._lugar = lugar
        self._fecha = fecha
        self._hora = hora
        self._costo = costo
        self._total: int = 0
        #self._configurar()

    @property
    def lugar(self) -> str:
        return self._lugar

    @lugar.setter
    def lugar(self, lugar: str) -> None:
        self._lugar = lugar

    @property
    def info(self) -> str:
        return (
            f"{f'{self._fecha}':^36}"
            f" {f'{self._hora}':^12} {f'S/.{self._costo}':^12}"
        )

    @info.setter
    def info(self, info: str) -> None:
        self._info = info

    def comprar(self) -> None:
        self.game.add_user(agregar_usuario(METODOS, self._costo))
        self._fecha_hora()
        print("Compra realizada correctamente")

    def visualizar(self) -> None:
        print(f"Usuarios: {len(self.game.usuarios)}")
        print(f"{self.game.usuarios}")

    def informacion(self, obj) -> None:
        self._configurar(*modificar_informacion())
        obj.subtitle = yellow(self.lugar)
        obj.prologue_text = cyan(self.info)

    def _configurar(
        self, lugar: str, fecha: str, hora: str, costo: str
    ) -> None:
        self.lugar = lugar
        self._fecha = fecha
        self._hora = hora
        self._costo = costo
        self.info = (
            f"{f'{self._fecha}':^36}"
            f" {f'{self._hora}':^12} {f'S/.{self._costo}':^12}"
        )

    def _fecha_hora(self) -> None:
        self._fecha = datenow("%d/%m/%Y")
        self._hora = datenow("%H:%M")

    def run(self) -> None:
        self.game.start()


def main():
    app = App(LUGAR, FECHA, HORA, COSTO)
    app.game.add_user(("Bot", "11001100", "bot@py.com", 1, "VISA"))
    menu = Menu(
        cyan("BINGO"),
        yellow(app.lugar),
        cyan(app.info),
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ("Comprar cartones", app.comprar),
        ("Visualizar compras", app.visualizar), # TODO
        ("Configurar", app.informacion, menu),
        ("Jugar BINGO", app.run),
    )
    menu.settings(
        subtitle_align="center",
        style="double",
        color=magenta,
        options_color=yellow,
        separators=True,
    )
    menu.run()


if __name__ == '__main__':
    main()