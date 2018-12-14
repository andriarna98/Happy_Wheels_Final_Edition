#Controllers
from Controller.Rent_controller import Rent_controller
from Controller.Order_controller import Order_controller
#Repos
from Repository.Log_repo import Log_repo
#Services
from Services.Salesman_service import Salesman_service
#UIs
from UI.Print_main_menu import Print_main_menu
from UI.Print_salesman_menu import Print_salesman_menu
from UI.Print_error import Print_error
#Utilizations
from Utilizations.Salesman_validation import Salesman_validation
from Utilizations.Format_text import Format_text
# OS
import os

class Salesman_controller:
    def __init__(self):
        #Controllers
        self.__rent_controller = Rent_controller()
        self.__order_controller = Order_controller()
        #Services
        self.__salesman_service = Salesman_service()
        #UI
        self.__salesman_menu = Print_salesman_menu() 
        self.error = Print_error()
        #Utilizations
        self.__Salesman_valid = Salesman_validation()
        self.__get_format = Format_text()
        #Variables
        self.confirmation_str = ""
        self.menu = ""
        self.underline = ""
        
    def sign_in_page(self):
        """Gets employee's ID and password and checks if it's valid"""
        # Get ID
        self.menu = self.__get_format.log_in_format()
        self.__ID = self.__salesman_menu.ID_menu(self.menu)
        # Get password
        self.__password = self.__salesman_menu.password_menu(self.menu, self.__ID)
        # Check whether it's valid or not
        valid = self.__salesman_service.salesman_ID_pw(self.__ID,self.__password)
        if valid == False:
            try_again = input("\n\t\tID or password is invalid. Try again? (y/n): ").lower()
            return try_again, valid
        else:
            return "n", valid

    def salesman_menu(self): 
        Page = 1
        while 0 < Page < 4:           
            if Page == 1:
                # Prints Salesman menu
                self.menu, self.underline = self.__get_format.salesman_format()
                choice = self.__salesman_menu.salesman_main_page(self.menu, self.underline)
                Valid, Page = self.__Salesman_valid.Check_menu_choice(choice, Page)
                if Valid:
                    Page += 1 # Moves to next page
                elif Page == 0:
                    pass    # Moves to previous page
                elif Page != 4:
                    self.error.Wrong_salesmanmenu_choice() # Prints error message

            elif Page == 2:
                # Search for order
                if choice == "1":
                    Page = self.__order_controller.find_order_process(Page)

                # Get customer information
                elif choice == "2":
                    self.menu = self.__get_format.customer_info_format()
                    self.email = self.__salesman_menu.customer_info_menu(self.menu)
                    Page = self.__Salesman_valid.Check_email_choice(self.email, Page)
                    if Page == 2:
                        customer = self.__salesman_service.get_customer(self.email)
                        if customer == None:
                            self.error.Wrong_email()
                        else:
                            orders = self.__salesman_service.order_string()
                            delete = self.__salesman_menu.customer_list(self.underline ,customer, orders)
                            if delete == "d":
                                self.__salesman_service.delete_customer(customer)
                                self.confirmation_str = "Customer"
                                action = "removed"
                                self.__salesman_service.delete_customer_to_log(self.__ID)
                                self.__salesman_menu.confirmation(self.confirmation_str, action)
                        
                # Get cars information
                elif choice == "3":
                    self.menu = self.__get_format.car_info_format()
                    self.__choice = self.__salesman_menu.cars_info_menu(self.menu, self.underline)
                    Valid, Page = self.__Salesman_valid.Check_cars_information_choice(self.__choice, Page)
                    if Valid:
                        pass    # Moves forward
                    elif Page == 1:
                        pass    # Moves to previous page
                    elif Page != 8:
                        self.error.Wrong_car_info_choice() # Prints error message

                    if Page == 2:
                        if self.__choice == "1":
                            self.cars = self.__salesman_service.get_all_cars()

                        elif self.__choice == "2":
                            self.cars = self.__salesman_service.get_available_cars()

                        elif self.__choice == "3":
                            self.cars = self.__salesman_service.get_unavailable_cars()

                        elif self.__choice == "4":
                            self.menu = self.__get_format.add_car_format()
                            plate_num, brand, size, location = self.__salesman_menu.add_car(self.menu)
                            if plate_num != "p":
                                self.__salesman_service.add_car_repo(plate_num, brand, size, location)
                                self.confirmation_str = "Car"
                                action = "added"
                                self.__salesman_menu.confirmation(self.confirmation_str, action)
                                # Add to log
                                self.__salesman_service.add_to_log(self.__ID, brand, plate_num)

                        # Returns results from user's choice (all cars, available cars or unavailable cars)
                        if self.__choice in ["1","2","3"]:
                            os.system("cls||clear")
                            self.menu = self.__get_format.car_list_format(self.__choice)
                            self.__salesman_menu.car_list_header(self.menu)
                            if self.cars != []:
                                for car in self.cars:
                                    plate_number = car.get_plate_number()
                                    brand = car.get_brand()
                                    location = car.get_location_string()
                                    self.__salesman_menu.car_lists(plate_number, brand, location)
                                    Page = 1
                                input("\n\t\t\tPress enter to continue ")
                            else:
                                self.__salesman_menu.no_cars()
                                input("\n\t\t\tPress enter to continue ")

                elif choice == "4":
                    self.menu = self.__get_format.log_format()
                    log = self.__salesman_service.get_log()
                    self.__salesman_menu.print_log(self.menu, self.underline, log)
                    Page = 1

                elif choice == "5":
                    self.menu = self.__get_format.password_format()
                    new_pw = self.__salesman_menu.get_new_pw(self.menu)
                    self.__salesman_service.change_pw(new_pw)
                    Page = 1
                    input("\n\t\t\tPress enter to continue ")
            