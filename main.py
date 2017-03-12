import tkinter as tk
from window import StartPage

LARGE_FONT = ("Verdana",12)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        self.frameList = [StartPage]

        for F in self.frameList:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Application()
app.geometry("640x480")
app.title("Universal Mod Manager")
app.resizable(width=False,height=False)
app.mainloop()