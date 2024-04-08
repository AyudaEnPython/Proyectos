"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
VARIANTS = {
    "Voltaje": ("Intensidad", "*" , "Resistencia"),
    "Intensidad": ("Voltaje", "/","Resistencia"),
    "Resistencia": ("Voltaje", "/", "Intensidad"),
}


def _clean(ws):
    for w in ws:
        w.delete(0, "end")


def _table(x, y, s):
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y,
    }[s]


def calculate(x, op, y, r):
    try:
        t = _table(float(x.get()), float(y.get()), op)
    except ValueError:
        r.config(text="Valores incorrectos")
        _clean((x, y))
    except ZeroDivisionError:
        r.config(text="Error, división entre cero")
        _clean((x, y))
    else:
        r.config(text=t)
