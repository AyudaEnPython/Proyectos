from tkinter import Tk, Canvas


class CustomCanvas(Canvas):

    def __init__(self):
        super().__init__()



class App(Tk):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = App()
    app.mainloop()
