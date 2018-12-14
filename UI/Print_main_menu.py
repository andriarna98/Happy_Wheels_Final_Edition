#Os
import os

class Print_main_menu:
    def __init__(self):
        pass

    def main_page(self,header,menu,choices,underline):
        """ Prints out the main menu for the user """
        os.system('cls||clear')
        print(header, end="\n\n")
        print(menu, end="\n\n")
        print(choices, end="\n")
        print(underline)
        choice = input("\t\t\t\t\tChoose an option: ").lower()
        return choice