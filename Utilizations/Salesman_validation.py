
class Salesman_validation:
    def __init__(self):
        pass

    def Check_if_nav(self, choice, page):
        """ Checks if user input is p for previous, h for home or x for exit
        before doing anything else then  """
        if choice == "p":   # Goes to previous page - if page == 12(receipt page), then user can not go back
            page -= 1
        elif choice == "m": # Goes back to start of program 
            page = 4
        elif choice == "x": # Exits 
            exit()
        return page

    def Check_menu_choice(self, choice, page):
        self.__check_nav = Salesman_validation() # Makes instance of Rent_validation class to call Check_if_nav, used in all Check functions
        page = self.__check_nav.Check_if_nav(choice, page)
        if choice in ("1", "2", "3", "4", "5", "6"):
            return True, page
        else:
            return False, page

    def Check_cars_information_choice(self, choice, page):
        self.__check_nav = Salesman_validation()
        page = self.__check_nav.Check_if_nav(choice, page)
        if choice in ("1", "2", "3", "4"):
            return True, page
        else:
            return False, page

    def Check_navigation(self, choice, page):
        self.__check_nav = Salesman_validation()
        page = self.__check_nav.Check_if_nav(choice, page)
        return page

    def Check_email_choice(self, choice, page):
        self.__check_nav = Salesman_validation()
        page = self.__check_nav.Check_if_nav(choice, page)
        return page