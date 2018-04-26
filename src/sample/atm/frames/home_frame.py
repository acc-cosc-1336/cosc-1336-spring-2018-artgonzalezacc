from tkinter import Frame, Label, Button
import random

class HomeFrame(Frame):
    """Frame container for the home screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text='ACME Banking: ').grid(row=0, column=0)

        Button(self, text='Start', command=self.start_button_handler).grid(row=1, column=0)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def start_button_handler(self):

        atm_frame = self.master.master.frames['ATMFrame']
        atm_frame.main_menu_actions.atm.customer = atm_frame.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]
        self.master.master.show_frame('AccountFrame')

    

