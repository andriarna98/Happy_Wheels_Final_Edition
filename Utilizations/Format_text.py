#Tabulate
from tabulate import tabulate

class Format_text:
    def __init__(self):
        pass
    
    ######### Rent process ##########
    def main_menu_format(self):
        header = tabulate([["Press 'I' for information\t\t\t\t\t\tPress 'X' for exit"]], tablefmt="plain")
        formatted_header = ''.join('{:^50}'.format(s) for s in header.split('\n'))
        main_menu = tabulate(["~MAIN MENU~"], tablefmt="fancy_grid")
        formatted_main_menu = '\n'.join('{:^100}'.format(s) for s in main_menu.split('\n'))
        choices = tabulate([["1. Continue as a Customer"],["2. Continue as a Salesman"], \
        ["3. Cancel an existing order"]], tablefmt="plain")
        formatted_choices = '\n'.join('{:^100}'.format(s) for s in choices.split('\n'))
        underline = "-" * 40
        formatted_underline = '\n'.join('{:^100}'.format(s) for s in underline.split('\n'))

        return formatted_header, formatted_main_menu, formatted_choices, formatted_underline

    def loc_format(self):
        location_menu = tabulate(["~LOCATION~"], tablefmt="fancy_grid")
        formatted_loc_menu = '\n'.join('{:^80}'.format(s) for s in location_menu.split('\n'))
        page = tabulate([["Page 1 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))
        choices = tabulate([["1. Reykjavík"],["2. Keflavík"],["3. Akureyri"]], tablefmt="plain")
        formatted_choices = '\n'.join('{:^80}'.format(s) for s in choices.split('\n'))
        underline = "-" * 40
        formatted_underline = '\n'.join('{:^80}'.format(s) for s in underline.split('\n'))

        return formatted_loc_menu, formatted_page, formatted_choices, formatted_underline
    
    def date_time_format(self):
        date_time_menu = tabulate(["~DATE AND TIME~"], tablefmt="fancy_grid")
        formatted_date_time_menu = '\n'.join('{:^80}'.format(s) for s in date_time_menu.split('\n'))
        page = tabulate([["Page 2 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))
        
        return formatted_date_time_menu, formatted_page
    
    def car_format(self):
        car_size_menu = tabulate(["~PICK A CAR~"], tablefmt="fancy_grid")
        formatted_size_menu = '\n'.join('{:^80}'.format(s) for s in car_size_menu.split('\n'))
        page = tabulate([["Page 3 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))
        choices = tabulate([["1. Small cars ...7500 kr."],["2. Medium cars ...11500 kr."],
        ["3. SUV ...15000 kr."]], tablefmt="plain")
        formatted_choices = '\n'.join('{:^80}'.format(s) for s in choices.split('\n'))
        
        return formatted_size_menu, formatted_page, formatted_choices
    
    def feature_format(self):
        feature_menu = tabulate(["~ADDITIONAL FEATURES~"], tablefmt="fancy_grid")
        formatted_feature_menu = '\n'.join('{:^80}'.format(s) for s in feature_menu.split('\n'))
        page = tabulate([["Page 4 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_feature_menu, formatted_page
    
    def order_format(self):
        order_menu = tabulate(["~ORDER~"], tablefmt="fancy_grid")
        formatted_order_menu = '\n'.join('{:^80}'.format(s) for s in order_menu.split('\n'))
        page = tabulate([["Page 5 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_order_menu, formatted_page
    
    def personal_info_format(self, section):
        personal_menu = tabulate(["~PERSONAL INFO {}~".format(section+1)], tablefmt="fancy_grid")
        formatted_personal_menu = '\n'.join('{:^80}'.format(s) for s in personal_menu.split('\n'))
        page = tabulate([["Page 6 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_personal_menu, formatted_page
    
    def payment_method_format(self):
        pay_method_menu = tabulate(["~PERSONAL INFO~"], tablefmt="fancy_grid")
        formatted_method_menu = '\n'.join('{:^80}'.format(s) for s in pay_method_menu.split('\n'))
        page = tabulate([["Page 7 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_method_menu, formatted_page
    
    def card_info(self):
        card_info_menu = tabulate(["~CARD INFO~"], tablefmt="fancy_grid")
        formatted_card_menu = '\n'.join('{:^80}'.format(s) for s in card_info_menu.split('\n'))
        page = tabulate([["Page 8 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_card_menu, formatted_page
    
    def insurance_info(self):
        insurance_menu = tabulate(["~INSURANCE~"], tablefmt="fancy_grid")
        formatted_incurance_menu = '\n'.join('{:^80}'.format(s) for s in insurance_menu.split('\n'))
        page = tabulate([["Page 8 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_incurance_menu, formatted_page
    
    def checkout_format(self):
        checkout_menu = tabulate(["~CHECKOUT~"], tablefmt="fancy_grid")
        formatted_checkout_menu = '\n'.join('{:^80}'.format(s) for s in checkout_menu.split('\n'))
        page = tabulate([["Page 9 of 9"]], tablefmt="plain")
        formatted_page = ''.join('{:^80}'.format(s) for s in page.split('\n'))

        return formatted_checkout_menu, formatted_page
    
    def receipt_format(self):
        receipt_menu = tabulate(["~RECEIPT~"], tablefmt="fancy_grid")
        formatted_receipt_menu = '\n'.join('{:^80}'.format(s) for s in receipt_menu.split('\n'))
        
        return formatted_receipt_menu
    
    ######## salesman process ########
    def log_in_format(self):
        log_in_menu = tabulate(["~LOG IN~"], tablefmt="fancy_grid")
        formatted_log_in_menu = '\n'.join('{:^80}'.format(s) for s in log_in_menu.split('\n'))

        return formatted_log_in_menu
    
    def salesman_format(self):
        salesman_menu = tabulate(["~SALESMAN MENU~"], tablefmt="fancy_grid")
        formatted_salesman_menu = '\n'.join('{:^80}'.format(s) for s in salesman_menu.split('\n'))
        underline = "-" * 45
        formatted_underline = '\n'.join('{:^80}'.format(s) for s in underline.split('\n'))

        return formatted_salesman_menu, formatted_underline
    
    def find_order_format(self):
        find_order_menu = tabulate(["~FIND ORDER~"], tablefmt="fancy_grid")
        formatted_order_menu = '\n'.join('{:^80}'.format(s) for s in find_order_menu.split('\n'))
        underline = "-" * 45
        formatted_underline = '\n'.join('{:^80}'.format(s) for s in underline.split('\n'))

        return formatted_order_menu, formatted_underline
    
    def customer_info_format(self):
        cust_info_menu = tabulate(["~CUSTOMER INFO~"], tablefmt="fancy_grid")
        formatted_cust_info_menu = '\n'.join('{:^80}'.format(s) for s in cust_info_menu.split('\n'))
        
        return formatted_cust_info_menu
    
    def car_info_format(self):
        car_info_menu = tabulate(["~CAR INFO~"], tablefmt="fancy_grid")
        formatted_car_info_menu = '\n'.join('{:^80}'.format(s) for s in car_info_menu.split('\n'))

        return formatted_car_info_menu
    
    def car_list_format(self, list_choice):
        car_list = ""
        if list_choice == "1":
            car_list = "ALL CARS"
        elif list_choice == "2":
            car_list = "AVAILABLE CARS"
        elif list_choice == "3":
            car_list = "UNAVAILABLE CARS"
        
        car_list_menu = tabulate(["~{}~".format(car_list)], tablefmt="fancy_grid")
        formatted_car_list_menu = '\n'.join('{:^80}'.format(s) for s in car_list_menu.split('\n'))

        return formatted_car_list_menu
    
    def add_car_format(self):
        add_car_menu = tabulate(["~ADD CAR~"], tablefmt="fancy_grid")
        formatted_add_car_menu = '\n'.join('{:^80}'.format(s) for s in add_car_menu.split('\n'))

        return formatted_add_car_menu

    def log_format(self):
        log_menu = tabulate(["~OPERATION LOG~"], tablefmt="fancy_grid")
        formatted_log_menu = '\n'.join('{:^80}'.format(s) for s in log_menu.split('\n'))

        return formatted_log_menu
    
    def password_format(self):
        pw_change_menu = tabulate(["~NEW PASSWORD~"], tablefmt="fancy_grid")
        formatted_pw_menu = '\n'.join('{:^80}'.format(s) for s in pw_change_menu.split('\n'))

        return formatted_pw_menu
    
    ###### information ######
    def info_format(self):
        info_menu = tabulate(["~HAPPY WHEELS~"], tablefmt="fancy_grid")
        formatted_info_menu = '\n'.join('{:^80}'.format(s) for s in info_menu.split('\n'))

        return formatted_info_menu
