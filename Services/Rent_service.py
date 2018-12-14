#Models
from Models.Car import Car
from Models.Order import Order
from Models.Customer import Customer
#Repos
from Repository.Cars_repo import Cars_repo
from Repository.Orders_repo import Orders_repo
from Repository.Customer_repo import Customer_repo
from Repository.Log_repo import Log_repo
#UIs
from UI.Print_error import Print_error
#Utilizations
from Utilizations.Rent_validation import Rent_validation
#Os, Datetime
import datetime, os

class Rent_service:
    def __init__(self):
        # Repos
        self.car_repo = Cars_repo()
        self.order_repo = Orders_repo()
        self.customer_repo = Customer_repo()
        # UI's
        self.error = Print_error()
        #Utilizations
        self.__Rent_valid = Rent_validation()
        self.log_repo = Log_repo()
        #List
        self.feature_list = []

    def change_str_to_date(self, num_list):
        """ Takes in a list with pick up and drop off string and returns a list with pick up and drop off dates."""
        pick_up_num, drop_off_num = num_list
        pick_up_date = datetime.date(int(pick_up_num[4:8]), int(pick_up_num[:2]), int(pick_up_num[2:4]))
        drop_off_date = datetime.date(int(drop_off_num[4:8]), int(drop_off_num[:2]), int(drop_off_num[2:4]))

        return [pick_up_date, drop_off_date] 
       
    def find_available_cars(self, date, size, location):
        """Get car_dict from repo and get inputs from Rent controller. 
        Compare to get available car."""
        self.available_car_list = []
        car_dict = self.car_repo.get_cars()
        for value in car_dict.values():
            if location == value.get_location() and size == value.get_car_size():
                new_pick_up_date, new_drop_off_date = date
                old_orders = value.get_orders()
                if old_orders != []:
                    for order in old_orders:
                        old_pick_up, old_drop_off = order
                        if (old_drop_off < new_pick_up_date and old_drop_off < new_drop_off_date) or \
                        (old_pick_up > new_pick_up_date and old_pick_up > new_drop_off_date): 
                            valid = True
                        else:
                            valid = False
                            break
                    if valid == True:
                        self.available_car_list.append(value)
                else:
                    self.available_car_list.append(value)                          
        return self.available_car_list

    def get_car_size_string(self, choice):
        """Converts choice of size (1,2,3) to a string which represents the size name (Small, Medium, SUVs)"""
        if choice == "1":
            string = "Small cars:"
        elif choice == "2":
            string = "Medium cars:"
        elif choice == "3":
            string = "SUVs:"
        return string

    def make_carlist_string(self, available_car_list):
        """Constructs a string made from the car_list to print out for the user"""
        carlist_string = ""
        for index, car in enumerate(available_car_list):
            carlist_string += ("\n\t\t\t  Car {:>3}: {:>12}{:>10} kr.".format(index+1, car.get_brand(), car.get_pri_ins()[0]))
        return carlist_string

    def get_desired_car(self, car_choice):
        """Uses self.user_input to index car in the car_list, makes the car object, self.desired_car"""
        num_choice = int(car_choice)
        self.desired_car = self.available_car_list[num_choice-1]
        return self.desired_car

    def desired_car_info(self):
        "Takes the desired car object and return all of its attributes in a string"
        string = ""
        string += "\t\t\t\t  ~~{}~~\n".format(self.desired_car.get_brand())
        string += "\n"
        string += "\t\t\t\tLocation: {}\n".format(self.desired_car.get_location_string())

        price, insurance = self.desired_car.get_pri_ins()
        string += "\t\t\t\tBase price: {} kr.\n\t\t\t\tInsurance: {} kr.".format(price, insurance)
        return string

    def get_feature_string(self, choice):
        """Converts user_input (1,2,3) to string (GPS, Baby chair, Extra Insurance)"""
        if choice == "1":
            return "GPS"
        elif choice == "2":
            return "Baby chair"
        elif choice == "3":
            return "Extra Insurance"
    
    def get_index(self):
        """Get index of the additional feature the user wants to remove"""
        for index, feature in enumerate(self.feature_list):
            if feature == self.user_input:
                return index

    def add_features(self, choice):
        """Adds features to list, returns list"""
        self.user_input = choice
        # Get string from the user_input which we then use when printing added! or removed! statements.
        feature_string = self.get_feature_string(choice)

        # Get index of the user_input to find it in the list, returns the index and then we
        # use the index to remove the feature from the list
        index = self.get_index()
        
        if choice not in self.feature_list:   # If valid feature and not already in feature_list
            print("\t\t\t\t{} added!".format(feature_string))
            self.feature_list.append(choice)
            input("\t\t\t\tPress enter to continue")
        elif choice in self.feature_list:  # If already in feature_list it is removed from it
            print("\t\t\t\t{} removed!".format(feature_string))
            self.feature_list.pop(index)
            input("\t\t\t\tPress enter to continue")
            
        return self.feature_list

    def reset_features(self):
        """ Resets the list of features """
        self.feature_list = []
        self.feature_string = ""
        return self.feature_list, self.feature_string

    def get_price(self, feature_list, car_obj):
        """Returns final price for the customer, takes the list of additional features and calculates the price."""
        price, insurance = car_obj.get_pri_ins()
        additional_price = int(insurance)
        for feature in feature_list:
            if feature == "1":
                additional_price += 5000
            elif feature == "2":
                additional_price += 1000
            elif feature == "3":
                additional_price += 6500
        return additional_price, int(price)

        
    def make_date_str(self, date):
        """Takes the self.__date_list and turns it into a string"""
        pick_up, drop_off = date
        date_info = "\t\t\t\tPickup date: {}\n\t\t\t\tDrop off date: {}".format(pick_up, drop_off)
        return date_info
    
    def make_feature_string(self, choice):
        feature_string = ""
        for choice in self.feature_list:
            feature_string += "\t\t\t\t{}\n".format(self.get_feature_string(choice))
        if feature_string == "":
            return "None\n"
        return feature_string

    def make_booking_num(self):
        """Makes booking number from order dictionary"""
        book_list = []
        for key, values in self.order_repo.get_orders().items(): 
            for order in values:
                book_list.append(int(order.get_order_num()))
        if book_list != []:
            book_num = max(book_list) + 1
        else:
            book_num = 1
        return book_num

    def add_order_to_dict(self, booking_num, email, plate_num, date_list):
        """Adds order to order dictionary with all the information from the user input. Also updates order repository with
        the new dictionary"""
        new_pick_up, drop_off = date_list
        new_order = Order(booking_num, new_pick_up, drop_off, plate_num, email)
        order_dict = self.order_repo.get_orders()
        if order_dict != {}:
            for key, values in order_dict.items():
                if key == plate_num:
                    values.append(new_order)
                    break
                elif plate_num not in order_dict:
                    order_dict[plate_num] = [new_order]
                    break
        else:
            order_dict[plate_num] = [new_order]
        
        self.order_repo.update_order_file(order_dict)
    
    def update_customer_repo(self, new_customer):
        email = new_customer.get_email()
        customer_dict = self.customer_repo.get_customers()
        customer_dict[email] = new_customer
        self.customer_repo.add_customers(customer_dict)

    def update_log(self, first_name, last_name, car_obj, date_list):
        """Updates log repository when a customer books a car"""
        update_repo = self.log_repo
        update_repo.Update_repo("{} {} booked {}, {}. Pick up date: {}, Drop off date {}\n".format(first_name, last_name, car_obj.get_brand(), car_obj.get_plate_number(), date_list[0], date_list[1]))
