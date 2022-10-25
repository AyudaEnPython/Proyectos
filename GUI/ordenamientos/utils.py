"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import List


def color(arr: List[int], c: str) -> List[str]:
    return [c for _ in range(len(arr))]


def generate_data(
    min: int = 0,
    max: int = 20,
    size: int = 20,
) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def normalize(arr: List[int]) -> List[int]:
    return [x/max(arr) for x in arr]
