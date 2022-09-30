"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import sleep
# pip install prototools
from prototools import Menu, ProtoDB, textbox, progressbar
from prototools.colorize import green, yellow, magenta, cyan, red

data = ProtoDB("songs")
ALBUM = data.get_data()


def play(song):
    print()
    textbox(
        yellow(f"{song['title']} - {song['artist']}"),
        light=False, bcolor="magenta", width=56, ml=1,
    )
    for _ in progressbar(
        range(int(song['duration'])*10),
        width=51, units=False, per=False,
        spinvar_color=red, fg=green, bg=cyan,
    ):
        sleep(0.1)


def main():
    menu = Menu(
        green("Jukebox"),
        yellow("Simple CLI Jukebox"),
        yellow("Playlist"),
        yellow("Selecciona una opción"),
        exit_option_text=magenta("Finalizar"),
        exit_option_color=magenta,
        arrow_keys=True,
    )
    for song in ALBUM:
        menu.add_option(
            "{} {}".format(
                green(f"({song['duration']:.2f})"),
                cyan(f"{song['title']} {song['artist']}")),
            play, [song],
        )
    menu.settings(
        dimension=(60, 20),
        style="double",
        color=magenta,
        options_color=yellow,
        separators=True,
        paddings=(1, 1, 0, 0),
        items_paddings=(1, 1, 1, 1),
        subtitle_align="center",
    )
    menu.run()


if __name__ == "__main__":
    main()
