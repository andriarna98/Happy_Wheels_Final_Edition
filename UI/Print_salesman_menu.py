#Os
import os

class Print_salesman_menu:

    def __init__(self):
        #Headers
        self.main_header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"        
        
    def ID_menu(self, menu):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        id = input("\t\t\t\tEnter your ID: ")
        return id
    
    def password_menu(self, menu, id):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\t\t\t ID:", id)
        password = input("\t\t\t Enter your password: ") 
        return password
    
    def salesman_main_page(self, menu, underline):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\t\t  1. Search for order\t  4. Operation LOG")
        print("\t\t  2. Customer information 5. Change password")
        print("\t\t  3. Cars information")
        print(underline)
        choice = input("\t\t\t\tChoose an option: ")
        return choice

    def cars_info_menu(self, menu, underline):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\t\t\t1. Overview of all cars")
        print("\t\t\t2. Overview of all available cars")
        print("\t\t\t3. Overview of all unavailable cars")
        print("\t\t\t4. Add car")
        print(underline)
        choice = input("\t\t\tChoose an option: ")
        return choice
    
    def car_list_header(self, menu):
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
    
    def customer_info_menu(self, menu):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        self.email = input("\t\t\tEnter customer email: ")
        return self.email


    def customer_list(self, underline, customer, orders):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print('\t\t\tEmail: {}'.format(self.email))
        print(underline)
        print("\t\t\t~~Customer information~~\n")
        print(customer)
        print("\n\t\t\t~~Customer orders~~")
        print(orders)
        delete = input("\n\t\t\tPress d to delete customer: ")
        return delete

    def car_lists(self, plate, brand, location):
        print("Plate number: {:10}\tBrand: {:10}\tLocation: {:10}".format(plate,brand,location))

    def get_new_pw(self, menu):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        new_pw = input("\t\t\t\tEnter new password: ")
        print("\n\t\t\tPassword changed!")
        return new_pw
    
    def print_orders(self, num, order):
        print("\t~Find order~\n")
        print("{}\n{}".format(num, order))

    def print_log(self, menu, underline, log):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\n"+log)
        input("\t\t\tPress enter to continue")

    def confirmation(self, confirmation_str, action):
        """Prints out confirmation string"""
        print("\t\t\t{} successfully {}!\n".format(confirmation_str, action))
        input("\t\t\tPress enter to continue.")

    def add_car(self, menu):
        os.system("cls||clear")
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\t\tSizes: 1 = Small car - 2 = Medium car - 3 = SUV")
        print("\t\tLocations: 1 = Reykjavík - 2 = Keflavík - 3 = Akureyri\n")
        plate_num = input("\t\t\tEnter plate number: ")
        brand = input("\t\t\tEnter car brand: ")
        size = input("\t\t\tEnter car size type (1,2,3): ")
        location = input("\t\t\tEnter location (1,2,3): ")
        return plate_num, brand, size, location 
        
    def print_cust_order(self, order):
        print(order)

    def no_cars(self):
        print("\t\t\tNo cars in this category.")