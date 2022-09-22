"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


# Taken from:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_bubble_sort.py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
