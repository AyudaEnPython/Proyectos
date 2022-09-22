"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import List 


def generate_data(
    min: int = 1,
    max: int = 100,
    size: int = 20,
) -> List[int]:
    return [randint(min, max) for _ in range(randint(min, size))]
