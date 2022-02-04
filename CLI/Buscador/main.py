"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys
from textwrap import dedent
from typing import Callable
import requests


BASE_URL = "https://api.github.com/search/code?q="
REPO = "AyudaEnPython/Soluciones"
LANGUAGE = "python"

QUERY = "{}+in%3afile+language%3a{}+repo%3a{}"
URL = BASE_URL + QUERY


def _action(s: str) -> Callable:
    actions = {
        "-s": search,
        "-h": help,
    }
    return actions[s]


def help() -> None:
    print("""
    AyudaEnPython: https://www.facebook.com/groups/ayudapython
    """)
    print(dedent("""\
        -s <search>: Buscar en el repositorio
        -h <help>: Ayuda

        Ejemplo:
        > python search.py -s poligono
    """))


def search(keyword: str) -> None: 
    response = requests.get(URL.format(keyword, LANGUAGE, REPO))
    data = response.json()["items"]

    print(f"Encontrados: {len(data)}\n")
    for item in data:
        print(item["path"])


def main():
    try:
        _action(sys.argv[1])(sys.argv[2])
    except Exception as e:
        print(e)
        help()


if __name__ == "__main__":
    main()