"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import sleep
from utils import color


# Taken from:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_bubble_sort.py
def bubble_sort(arr, f, timer: float):
    n = len(arr)
    for i in range(n):
        # swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # swapped = True
                f(
                    arr,
                    [
                        "cyan" if _ == j + 1 else "grey40"
                        for _ in range(len(arr))
                    ]
                )
                sleep(timer)
        # if not swapped:
            # break
    f(arr, color(arr, "green"))
    # return arr


# Taken from:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_insertion_sort.py
def insertion_sort(arr, f, timer: float):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        f(
            arr,
            [
                "cyan" if _ == i or _ == i + 1 else "grey40"
                for _ in range(len(arr))
            ]
        )
        sleep(timer)
        while j >= 0 and key < arr[j]:
            f(
                arr,
                [
                    "cyan" if _ == j or _ <= i else "grey40"
                    for _ in range(len(arr))
                ]
            )
            sleep(timer)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    f(arr, color(arr, "green"))
    # return arr
