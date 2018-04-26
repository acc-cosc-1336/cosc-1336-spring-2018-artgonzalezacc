from tkinter import Frame, Label, Button, Toplevel, Entry
from main_menu_actions import MainMenuActions

class ATMFrame(Frame):
    """Frame container for the Main ATM screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.main_menu_actions = MainMenuActions()

        Label(self, text='ACME ATM: ')

        Button(self, text='Deposit', command=self.button_deposit_handler).grid(row=2, column=0)
        Button(self, text='Withdraw', command=self.button_withdraw_handler).grid(row=3, column=0)
        Button(self, text='Inquiry', command=self.button_inquiry_handler).grid(row=4, column=0)
        Button(self, text='Transactions').grid(row=5, column=0)
        Button(self, text='Exit', command=lambda:self.master.master.show_frame('AccountFrame')).grid(row=6, column=0)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def button_deposit_handler(self):

        self.top = Toplevel(self)
        self.text_box_amount = Entry(self.top)
        self.text_box_amount.pack()
        Button(self.top, text='ok', command=self.deposit_dialog_handler).pack()

    def deposit_dialog_handler(self):

        self.main_menu_actions.handle_deposit(int(self.text_box_amount.get()))
        self.top.destroy()
        
    def button_withdraw_handler(self):

        self.top = Toplevel(self)
        self.text_box_amount = Entry(self.top)
        self.text_box_amount.pack()
        Button(self.top, text='ok', command=self.deposit_dialog_handler).pack()

    def withdraw_dialog_handler(self):

        self.main_menu_actions.handle_withdraw(int(self.text_box_amount.get()))
        self.top.destroy()

    def button_inquiry_handler(self):
        self.top = Toplevel(self)
        Label(self.top, text=self.main_menu_actions.get_inquiry_balance()).pack()
        Button(self.top, text='ok', command=self.inquiry_dialog_handler).pack()

    def inquiry_dialog_handler(self):

        self.top.destroy()


