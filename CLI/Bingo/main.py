"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu
from prototools.colorize import magenta, cyan, yellow
from bingo.bingo import Game
from bingo.utils import agregar_usuario, datenow
from bingo import PRECIO


class App:

    def __init__(self) -> None:
        self.game = Game()
        self.configurar()

    def comprar(self):
        self.game.add_user(agregar_usuario())
        self.fecha_hora()
        print("Compra realizada correctamente")

    def visualizar(self):
        print(f"Usuarios: {len(self.game.usuarios)}")
        print(f"{self.game.usuarios}")

    def fecha_hora(self):
        self._fecha = datenow("%d/%m/%Y")
        self._hora = datenow("%H:%M")

    def run(self):
        self.game.start()
    
    def configurar(self):
        self.lugar = "Comunidad Ayuda En Python"
        self._fecha = "24 de diciembre del 2021"
        self._hora = "19:00"
        self.info = (
            f"{f'{self._fecha}':^26}"
            f" {f'{self._hora}':^26} {f'S/.{PRECIO}':^26}"
        )


def main():
    app = App()
    app.game.add_user(("Bot", "11001100", "bot@py.com", 1, "VISA"))
    menu = Menu(
        cyan("BINGO"),
        app.lugar,
        app.info,
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ("Comprar cartones", app.comprar),
        ("Visualizar compras", app.visualizar),
        ("Configurar", lambda: print()),
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