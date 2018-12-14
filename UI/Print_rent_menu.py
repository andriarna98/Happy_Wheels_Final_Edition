#Models
from Models.Customer import Customer
#Os
import os

class Print_rent_menu:
    def __init__(self):
        #Headers
        self.main_header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"
        self.receipt_header = "Press 'm' for Main menu\t\t\t\t\tPress 'x' to Exit"

    def Page_1(self, menu, page, choices, underline):
        """ Prints out the menu where the customer chooses 
        location to pick up his desired car """
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print("\t\t\t\tSelect pick up location:", end="\n")
        print(choices, end="\n")
        print(underline)
        choice = input("\t\t\t\tChoose an option: ").lower()

        return choice

    def Page_2(self, menu, page):
        """ Prints out the menu where the customer chooses 
        date to pick up his desired car """
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        pick_up_date = input("\t\t\tEnter pick up date(mmddyyyy): ")
        drop_off_date = input("\t\t\tEnter drop off date(mmddyyyy): ")

        return [pick_up_date, drop_off_date]

    def Page_3(self, menu, page, choices, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print(choices, end="\n") # Hér er hægt að vera búinn að vera með breytu
        print(underline)    # sem eru cheapest og most expensive bílar
        choice = input("\t\t\tChoose your vehicle size: ").lower()

        return choice
    
    def Page_4(self, menu, page, underline, available_car_string, size_string):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")    
        print("\t\t\t\t  " + size_string)  # Kallar á samansettan streng
        print(available_car_string) # Kallar á samansettan streng
        print(underline)
        choice = input("\t\t\tChoose your desired car number: ").lower()

        return choice
        
    def Page_5(self, menu, page, underline, car_info):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print(car_info)
        print(underline)
        choice = input("\t\t\t\tPress 'c' to confirm: ").lower()

        return choice
        
    def Page_6(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print("\t\t\t1. GPS ...5.000 kr.")
        print("\t\t\t2. Baby chair ...1.000 kr.")   # Breyta í e-ð annað
        print("\t\t\t3. Insurance (extra) ...6.500 kr.\n")
        print("\t\t\tPress 'c' to continue to check out.\n\t\t\tTo remove a selected feature," 
        "\n\t\t\tpress the assigned number again.")
        print(underline)
        choice = input("\t\t\t\tChoose an option: ")
        
        return choice
    
    def Page_7(self, menu, page, underline, car_info, price, date_info, features):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print(car_info, end="\n")
        print(date_info, end="\n")
        print("\n\t\t\t\t~~Additional features~~")
        print(features)
        print("\t\t\t\tFinal price: {}".format(price))
        print(underline)
        choice = input("\t\t\t\tPress 'c' to confirm: ").lower()

        return choice

    def Page_8_1(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        first_name = input("\t\t\t\tEnter first name: ")
        last_name = input("\t\t\t\tEnter last name: ")
        date_of_birth = input("\t\t\t\tEnter date of birth(mmddyyyy): ")
        email = input("\t\t\t\tEnter email: ")
        print(underline)
        choice = input("\t\t\t\tPress 'c' to confirm: ").lower()

        return first_name, last_name, date_of_birth, email, choice

    def Page_8_2(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        country = input("\t\t\t\tEnter country: ")
        address = input("\t\t\t\tEnter address: ")
        zip_code = input("\t\t\t\tEnter zip code: ")
        phone = input("\t\t\t\tEnter phone number: ")
        print(underline)
        choice = input("\t\t\t\tPress 'c' to confirm: ").lower()

        return country, address, zip_code, phone, choice
    
    def Page_9(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print("\t\t\t1. Pay now with credit card")
        print("\t\t\t2. Pay now with debit card.")
        print("\t\t\t3. Pay when I pick up.")
        print(underline)
        choice = input("\t\t\tChoose payment method: ")

        return choice
    
    def Page_10_1(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        card_num = input("\t\tInput card number(xxxx xxxx xxxx xxxx): ")
        security_code = input("\t\t\tInput security code(xxx): ")
        exp_date = input("\t\t\tEnter expiration date(mmyy): ")
        print(underline)
        choice = input("\t\t\tPress 'c' to confirm: ").lower()

        return card_num, security_code, exp_date, choice

    def Page_10_2(self, menu, page, underline):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print("\t\tEnter your creditcard information for insurance")
        card_num = input("\t\tInput card number(xxxx xxxx xxxx xxxx): ")
        security_code = input("\t\t\tInput security code(xxx): ")
        exp_date = input("\t\t\tEnter expiration date(mmyy): ")
        print("\n\t\tIf you do not show up or forget to cancel order, " \
        "\n\t\tthe company will charge you full price.")
        print(underline)
        choice = input("\t\t\tPress 'c' to confirm: ").lower()

        return card_num, security_code, exp_date, choice
    
    def Page_11(self, menu, page, underline, new_customer, car_info, date_info, feature_string):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n")
        print(page, end="\n\n")
        print(new_customer, end="\n\n")
        print(car_info)
        print(date_info)
        print(feature_string)
        print(underline)
        choice = input("\t\t\t\tPress 'c' to confirm: ").lower()

        return choice

    def Page_12(self, menu, underline, booking_num):
        os.system('cls||clear')
        print(self.receipt_header, end="\n\n")
        print(menu, end="\n\n")        
        print("\t\t\tThanks for using our service"
        "\n\t\t\tand hope to see you soon!")
        print("\t\t\tYour booking number is: {}\n".format(booking_num))
        print("\t\t\tThe receipt will be sent to your email, " 
        "\n\t\t\talong with the booking number.")
        print(underline)
        input("\t\t\tPress enter to go back to main menu ")
        
