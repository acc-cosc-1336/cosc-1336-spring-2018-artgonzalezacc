from tkinter import Tk
from src.homework.widget.main_frame import MainFrame

class ClockApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        frame = MainFrame(self)
        frame.pack()

if __name__ == '__main__':
    app = ClockApp()
    app.mainloop()
