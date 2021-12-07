"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import RangeDict
from typing import List, Dict, Tuple, Optional

PRECIO: int = 8
METODOS: Tuple[str] = ("VISA", "Transferencia BCP", "Yape")
RANGOS = ((1, 15), (16, 30), (31, 45), (46, 60), (61, 75))
INDEX = RangeDict({
    k:v for k, v in zip(
        RANGOS, ((0, -0,), (1, -15), (2, -30), (3, -45), (4, -60))
    )
})