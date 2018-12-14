#Repos
from Repository.Orders_repo import Orders_repo
#Services
from Services.Find_order_service import Find_order_service
#UIs
from UI.Print_find_order_menu import Print_find_order_menu
#Utilizations
from Utilizations.Salesman_validation import Salesman_validation
from Utilizations.Format_text import Format_text

class Order_controller:
    def __init__(self):
        #Services
        self.__find_service = Find_order_service()
        #UI
        self.__menu = Print_find_order_menu()
        #Utilizations
        self.__Salesman_valid = Salesman_validation()
        self.__get_format = Format_text() 
        #Variables
        self.menu = ""
        self.underline = ""
    
    def find_order_process(self, page):
        """ Finds order from user's input and deletes it from the database """
        self.menu, self.underline = self.__get_format.find_order_format()
        order_num = self.__menu.find_by_num(self.menu)
        Page = self.__Salesman_valid.Check_navigation(order_num, page)

        if Page == 2:
            order = self.__find_service.get_order(order_num)
            if order != None:
                choice = self.__menu.print_order(self.underline, order)
                if choice == "d":
                    self.__find_service.delete_order(order_num)
                    self.__menu.confirmation()
            else:
                self.__menu.No_match(order_num)
            return Page
        else: 
            return Page





