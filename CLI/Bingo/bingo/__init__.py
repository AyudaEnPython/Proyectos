"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import RangeDict
from typing import Tuple

LUGAR: str = "Comunidad Ayuda En Python"
FECHA: str = "24 de diciembre del 2021"
HORA: str = "19:00"
COSTO: int = 5
METODOS: Tuple[str] = ("VISA", "Transferencia BCP", "Yape")
RANGOS: Tuple[Tuple[int, int]] = (
    (1, 15), (16, 30), (31, 45), (46, 60), (61, 75)
)
INDEX = RangeDict({
    k:v for k, v in zip(
        RANGOS, ((0, -0,), (1, -15), (2, -30), (3, -45), (4, -60))
    )
})