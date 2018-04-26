from tkinter import Frame, Label, Button

class AccountFrame(Frame):
    """Frame container for the Account selection screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text='Select Account: ').grid(row=0, column=1)

        Button(self, text='Checking', command=self.button_checking_handler).grid(row=2, column=1)
        Button(self, text='Savings', command=self.button_savings_handler).grid(row=3, column=1)
        Button(self, text='Exit', command=lambda:self.master.master.show_frame('HomeFrame')).grid(row=4, column=1)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def button_checking_handler(self):

        self.master.master.frames['ATMFrame'].main_menu_actions.atm.account = 1
        self.master.master.show_frame('ATMFrame')

    def button_savings_handler(self):

        self.master.master.frames['ATMFrame'].main_menu_actions.atm.account = 2
        self.master.master.show_frame('ATMFrame')
