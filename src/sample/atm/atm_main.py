from main_menu import MainMenu

class Main:

    def run(self):
        self.main_menu = MainMenu()#create an instance of MainMenu
        self.main_menu.run_atm()

Main().run()
