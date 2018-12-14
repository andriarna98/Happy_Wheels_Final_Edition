#Controllers
from Controller.Rent_controller import Rent_controller
from Controller.Salesman_controller import Salesman_controller
from Controller.Order_controller import Order_controller
from Controller.Information_controller import Information_controller
#UIs
from UI.Print_main_menu import Print_main_menu
#Utilizations
from Utilizations.Format_text import Format_text

class Main_controller:
    def __init__(self):
        #Controllers
        self.__rent_controller = Rent_controller()
        self.__salesman_controller = Salesman_controller()
        self.__order_controller = Order_controller()
        self.__information_controller = Information_controller()
        #UI
        self.__main_menu = Print_main_menu()
        #Utilizations
        self.__get_format = Format_text()

    def main_page(self):
        """Reads choice and directs on a path depending on input"""
        choice = ""
        while choice != "x":
            header, main_menu, choices, underline = self.__get_format.main_menu_format()
            choice = self.__main_menu.main_page(header,main_menu,choices,underline)
            if choice == "1":
                self.__rent_controller.Rent_page()
            elif choice == "2":
                try_again = ""
                while try_again != "n":
                    try_again, valid = self.__salesman_controller.sign_in_page()
                if valid == True:
                    self.__salesman_controller.salesman_menu()
            elif choice == "3":
                self.__order_controller.find_order_process(page=2)
            elif choice == "i":
                self.__information_controller.information_page()