#Models
from Models.Salesman import Salesman
#Services
from Services.Information_service import Information_service
#UIs
from UI.Print_information import Print_information
#Utilizations
from Utilizations.Format_text import Format_text
#Os

class Information_controller:
    def __init__(self):
        #Services
        self.info_service = Information_service()
        #UIs
        self.__information_menu = Print_information()
        #Utilizations
        self.__get_format = Format_text()
        #Variables
        self.menu = ""

    def information_page(self):
        """Reads choice and directs to right path depending on input"""
        choice = ""
        while choice not in ["p", "m"]:
            self.menu = self.__get_format.info_format()
            choice = self.__information_menu.information_main_page(self.menu)

            #Rental Agreement
            if choice == "1":
                self.__information_menu.car_rental_agreement()
                input("\nPress enter to continue.")

            #Terms and conditions
            elif choice == "2":
                self.__information_menu.terms_and_conditions()
                input("\nPress enter to continue.")

            #Quality Policy
            elif choice == "3":
                self.__information_menu.quality_policy()
                input("\nPress enter to continue.")

            #Uses salesman dict to return a dict of salesmen
            elif choice == "4":
                salesman_dict = self.info_service.get_salesman_dict()
                self.__information_menu.print_salesman_header()
                for ID, salesman in salesman_dict.items():
                    name = salesman.get_name()
                    email = salesman.get_email()
                    self.__information_menu.print_salesman(name, email, ID)
                input("\nPress enter to continue.")
                
            elif choice == "x":
                exit()