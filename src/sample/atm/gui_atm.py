from tkinter import Tk, Frame
from frames.home_frame import HomeFrame
from frames.account_frame import AccountFrame
from frames.atm_frame import ATMFrame

class GUIatm(Tk):

    def __init__(self):
        Tk.__init__(self, None, None)
        self.frames = {}
        self.__init_frames()

        self.mainloop()

    def __init_frames(self):

        container = Frame(self)
        container.grid(sticky="nswe")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for frame in (AccountFrame, ATMFrame, HomeFrame):

            current_frame = frame(container)

            self.frames[frame.__name__] = current_frame
            current_frame.grid(row=0, column=0, sticky="nswe")

    def show_frame(self, frame_name):

        frame = self.frames[frame_name]
        frame.tkraise()        

GUIatm()

        
