"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: get rid off magic numbers
"""
from turtle import Turtle, Screen, done

W, H = 600, 400
POSITIONS = [(x, 210-x) for x in range(60, 151, 30)]


def _draw(t, x, y, color, _f, *args):
    t.pu()
    t.setpos(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    _f(*args)
    t.end_fill()
    t.ht()


def _rect(t, w, h):
    for n in (w, h, w, h):
        t.fd(n)
        t.rt(90)


def _star(t):
    for _ in range(5):
        t.fd(50)
        t.rt(144)


def leaves(t, size, pos, color="forest green"):
    t.color(color)
    t.begin_fill()
    t.setpos(0, pos)
    t.setpos(size, pos - size)
    t.setpos(-size, pos - size)
    t.setpos(0, pos)
    t.end_fill()
    t.ht()


def trunk(t, color="chocolate"):
    w, h = W // 15, H // 8
    _draw(t, -(w//2), -90, color, _rect, t, w, h)


def snow(t, color="white"):
    _draw(t, -(W//2), -140, color, _rect, t, W, W//10)


def star(t, color="yellow"):
    _draw(t, -25, 170, color, _star, t)


def main():
    xmas = Screen()
    b, y, m, k = [Turtle() for _ in range(4)]
    xmas.tracer(0)
    xmas.setup(W, H)
    xmas.bgcolor("sky blue")
    trunk(y)
    snow(m)
    for size, pos in POSITIONS:
        leaves(b, size, pos)
    star(k)
    xmas.update()
    done()


if __name__ == "__main__":
    main()
