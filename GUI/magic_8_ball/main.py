"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Canvas, Frame, Label, simpledialog, Tk
from random import choice

RESPONSES = {
    "Es cierto": "It is certain",
    "Es decididamente así": "It is decidedly so",
    "Sin lugar a dudas": "Without a doubt",
    "Sí, definitivamente": "Yes definitely",
    "Puedes confiar en ello": "You may rely on it",
    "Como yo lo veo, sí": "As I see it, yes",
    "Lo más probable": "Most likely",
    "Perspectiva buena": "Outlook good",
    "Sí": "Yes",
    "Las señales apuntan a que sí": "Signs point to yes",
    "Respuesta confusa, vuelve a intentarlo": "Reply hazy, try again",
    "Vuelve a preguntar más tarde": "Ask again later",
    "Mejor no decirte ahora": "Better not tell you now",
    "No se puede predecir ahora": "Cannot predict now",
    "Concéntrate y vuelve a preguntar": "Concentrate and ask again",
    "No cuentes con ello": "Don't count on it",
    "Mi respuesta es no": "My reply is no",
    "Mis fuentes dicen que no": "My sources say no",
    "Las perspectivas no son muy buenas": "Outlook not so good",
    "Muy dudoso": "Very doubtful",
}
X = Y = 200
R = X - 20
FONT_STYLE = ("Courier", 8)
INNER = "midnight blue"
TEXT = "dodger blue"


class History:

    def __init__(self):
        self.history = []

    def save(self, question, answer):
        self.history.append([question, answer])

    def clear(self):
        self.history.clear()

    def __str__(self):
        return "\n".join(
            f"{question}: {answer}" for question, answer in self.history
        )


class Magic8Ball(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.setup_ui()

    def setup_ui(self):
        canvas = Canvas(self, width=400, height=400)
        self.create_circle(canvas, X, Y, R, "black")
        self.create_circle(canvas, X, Y-35, R*(5/9), "grey3")
        self._triangle_inverted(canvas)
        canvas.pack()
        self.answer = Label(
            self,
            text="",
            font=FONT_STYLE,
            bg=INNER,
            fg=TEXT,
            wraplength=80,
            justify="center",
        )
        self.answer.place(x=X, y=160, anchor="center")

    def create_circle(self, canvas, x, y, r, color):
        canvas.create_oval(
            (x-r, y-r, x+r, y+r),
            outline=color, fill=color, width=2,
        )

    def _triangle_inverted(self, canvas):
        a, b, c = 95, 95, 120
        canvas.create_polygon(
            (X-R+a, Y-R+b, X, Y+R-c, X+R-a, Y-R+b),
            outline=INNER, fill=INNER, width=2,
        )

    def set_answer(self, answer):
        answer += "."
        self.answer.config(text=answer)


class App(Tk):

    def __init__(self):
        super().__init__()
        self.history = History()
        self.title("Magic 8-Ball")
        self.language = "es"
        self._set_responses()
        self.setup_ui()

    def setup_ui(self):
        self.magic8ball = Magic8Ball(self)
        self.magic8ball.pack()
        self.btn = Button(self, text="Shake", command=self.shake)
        self.btn.pack()
    
    def _set_responses(self):
        if self.language == "es":
            responses = RESPONSES.keys()
        else:
            responses = RESPONSES.values()
        self.responses = tuple(responses)

    def shake(self):
        # question = simpledialog.askstring("Question", "Ask a question")
        answer = choice(self.responses)
        # if question:
        #     self.history.save(question, answer)
        self.magic8ball.set_answer(answer)

    def set_language(self):
        pass

    def display_history(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
