"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import requests
from bs4 import BeautifulSoup

URL = 'https://www.ratebeer.com/beer/top-50/'
page = requests.get(URL)


def main():
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("tr")
    for tr in elements[5:55]:
        td = tr.find_all("td")
        if len(td) > 0:
            for i in td:
                print(i.text, end=" ")
            print()


if __name__ == "__main__":
    main()
