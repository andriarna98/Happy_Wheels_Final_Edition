#Datetime
import datetime

class Rent_validation:
    def __init__(self):
        pass

    def Check_if_nav(self, choice, page):
        """ Checks if user input is p for previous, h for home or x for exit
        before doing anything else then  """
        if choice == "p" and page != 12:   # Goes to previous page - if page == 12(receipt page), then user can not go back
            page -= 1
        elif choice == "m": # Goes back to start of program 
            page = 13
        elif choice == "x": # Exits 
            exit()
        return page

    def Check_location(self, location, page):
        """ Checks if user input is a valid location """
        self.__check_nav = Rent_validation()    # Makes instance of Rent_validation class to call Check_if_nav, used in all Check functions
        page = self.__check_nav.Check_if_nav(location, page)    # Checks if user input is equal to p, m or X (navigation)
        if location in ("1", "2", "3"):
            return True, page
        else:
            return False, page

    def Check_date(self, dates, page): # mm//dd//yyyy
        for date in dates:
            page = self.__check_nav.Check_if_nav(date, page)    # Checks if user input is equal to p, m or X (navigation)
            if page != 2:
                return False, page
        pick_up = dates[0]
        drop_off = dates[1]
        # Time after exactly 5 years
        date_after_5years = datetime.date.today() + datetime.timedelta(365*5)  
        # Checks if dates are valid
        try:
            pickup_date = datetime.date(int(pick_up[4:8]), int(pick_up[:2]), int(pick_up[2:4]))
            dropoff_date = datetime.date(int(drop_off[4:8]), int(drop_off[:2]), int(drop_off[2:4]))
        except(ValueError):
            return False, page
        # Checks if pick_up- and drop_off dates are bigger than the date today and smaller than the date after 5 years
        # Also checks if pick_up date is smaller than drop_off date
        if datetime.date.today() <= pickup_date < date_after_5years \
            and datetime.date.today() < dropoff_date < date_after_5years \
            and pickup_date < dropoff_date:         
            return True, page
        else: 
            return False, page

    def Check_vehicle_size(self, vehicle_size, page):
        page = self.__check_nav.Check_if_nav(vehicle_size, page)    # Checks if user input is equal to p, m or X (navigation)
        if vehicle_size in ("1", "2", "3"):
            return True, page
        else:
            return False, page

    def Check_car_choice(self, car_choice, car_list, page):
        page = self.__check_nav.Check_if_nav(car_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        try:
            int(car_choice)
        except(ValueError):
            return False, page

        if 0 < int(car_choice) <= len(car_list):
            return True, page
        else:
            return False, page

    def Check_confirmation(self, choice, page):
        page = self.__check_nav.Check_if_nav(choice, page)  # Checks if user input is equal to p, m or X (navigation)    
        if choice == "c":
            return True, page
        else:
            return False, page

    def Check_feature(self, feature_choice, page):
        page = self.__check_nav.Check_if_nav(feature_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        if feature_choice in ("1", "2", "3", "c"):
            return True, page
        else:
            return False, page

    def Check_personal_info_1(self, info_list, page):   # first_name, last_name, date_of_birth, email
        """ Verifies first_name, last_name, date_of_birth and email,
        if the info given passes all the tests then this function returns True"""
        for info in info_list:    
            page = self.__check_nav.Check_if_nav(info, page)  # Checks if user input is equal to p, m or x (navigation)
            if page != 8:
                return False, page 

        for letter in info_list[:2]: 
            if not letter.isalpha():    # Checks if first  and last name only contains letters   
                return False, page

        try:    # Checks if date_of_birth is valid
            mm = info_list[2][:2]
            dd = info_list[2][2:4]
            yyyy = info_list[2][4:8]
            birthday = datetime.date(int(yyyy), int(mm), int(dd))
        except(ValueError):
            return False, page

        Twentyone_years = datetime.timedelta(365*21)
        
        if datetime.date.today() - birthday < Twentyone_years:    # Checks if user is atleast 21 years old
            return False, page

        check = 0
        for letter in info_list[3]: # Checks if '@' and '.' in email
            if letter == "@":
                check += 1
            elif letter == ".":
                check += 1
            if check == 2:
                break
        if check < 2:
            return False, page
        return True, page
            
    def Check_personal_info_2(self, info_list, page):
        """ Verifies country, zip_code and phone"""
        for info in info_list:    
            page = self.__check_nav.Check_if_nav(info, page)  # Checks if user input is equal to p, m or x (navigation)
            if page != 8:
                return False, page 

        for letter in info_list[0]: 
            if not letter.isalpha():    # Checks if country only contains letters   
                return False, page

        for number in info_list[2]:
            if number.isalpha():    # Checks if zip code contains only numbers
                return False, page

        for number in info_list[3]:
            if number.isalpha():    # Checks if phone number contains only numbers
                return False, page
        return True, page

    def Check_payment(self, payment_choice, page):
        page = self.__check_nav.Check_if_nav(payment_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        if payment_choice in ("1", "2", "3"):
            return True, page
        else:
            return False, page

    def Check_card_info(self, info_list, page): # card, security_code, exp_date, choice
        for info in info_list:    
            page = self.__check_nav.Check_if_nav(info, page)  # Checks if user input is equal to p, m or x (navigation)
            if page != 10:
                return False, page

        if info_list[3] != "c":
            return False, page

        # Strips spaces and dashes out of card number
        if " " in info_list[0]:
            info_list[0] = info_list[0].replace(" ", "")
        elif "-" in info_list[0]:
            info_list[0] = info_list[0].replace("-", "")

        # Checks if card number has length of 16 and security code has length of 3
        if len(info_list[0]) != 16 and len(info_list[1]) != 3 : # Checks if card number has length of 16 and security code has length of 3
            return False, page

        for number in info_list[0]: # Checks if card contains only numbers
            if number.isalpha():
                return False, page

        for number in info_list[1]: # Checks if security code contains only numbers
            if number.isalpha():
                return False, page

        # expiration date format: mmyy
        # mm = info_list[2][:2]
        # yy = info_list[2][2:4]
        # datet = '2015-12-15'

        # ExpirationDate = datetime.strptime(datet,"%Y-%m-%d").date()
        # now = date.today()
        # if ExpirationDate >= now:
        #     pass
        return True, page         