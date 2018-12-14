#Os
import os

class Print_find_order_menu:
    def __init__(self):
        self.main_header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"        

    def find_by_num(self, menu):
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        order_num = input("\t\t\tEnter order number: ")

        return order_num

    def confirmation(self):
        print("\n\t\t\tOrder successfully canceled!")
        input("\t\t\tPress enter to continue ")

    def print_order(self, underline, order):
        print("\n"+str(order))
        choice = input("\n\t\t\tPress d to delete order or enter to continue.").lower()

        return choice

    def No_match(self, order_num):
        print("\n\t\t\tInvalid order number: {} ".format(order_num))
        input("\t\t\tPress enter to continue ")
