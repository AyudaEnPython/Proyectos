from prototools import ProtoDB, Menu
from prototools.menu import Item


data = ProtoDB("songs")
ALBUM = data.get_data()


def main():
    menu = Menu("Jukebox")
    menu.set_dimension(width=60, height=20)
    menu.builder._header.show_bottom = True
    for song in ALBUM:
        menu.add_item(Item(f"({song['duration']:.2f}) {song['title']} {song['artist']}"))
    menu.run()


if __name__ == "__main__":
    main()