"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import RangeDict

PRECIO: int = 8
RANGOS = ((1, 15), (16, 30), (31, 45), (46, 60), (61, 75))
INDEX = RangeDict({
    k:v for k, v in zip(
        RANGOS, ((0, -0,), (1, -15), (2, -30), (3, -45), (4, -60))
    )
})