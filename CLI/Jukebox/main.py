from time import sleep
from prototools import ProtoDB, Menu, FunctionItem, textbox, progressbar
from prototools.colorize import *

data = ProtoDB("songs")
ALBUM = data.get_data()


def play(song):
    print()
    textbox(
        yellow(f"{song['title']} - {song['artist']}"),
        align="center",
        light=False,
        bcolor="magenta",
        width=58,
        ml=2,
    )
    for _ in progressbar(
        range(int(song['duration'])*10),
        width=52,
        units=False,
    ):
        sleep(0.1)


def main():
    menu = Menu(yellow("Jukebox"))
    menu.set_dimension(width=60, height=20)
    menu.builder._header.show_bottom = True
    for song in ALBUM:
        menu.add_item(FunctionItem(
            f"({song['duration']:.2f}) {song['title']} {song['artist']}",
            play,
            args=[song]
        ))
    menu.run()


if __name__ == "__main__":
    main()