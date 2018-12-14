#Models
from Models.Salesman import Salesman 
from Models.Customer import Customer
from Models.Car import Car
#Repos
from Repository.Cars_repo import Cars_repo
from Repository.Salesman_repo import Salesman_repo
from Repository.Customer_repo import Customer_repo
from Repository.Log_repo import Log_repo 
from Repository.Orders_repo import Orders_repo
#Datetime
import datetime

class Salesman_service:
    def __init__(self):
        #Repos
        self.cars_info = Cars_repo()
        self.salesman_info = Salesman_repo()
        self.customer_info = Customer_repo()
        self.log_repo = Log_repo()
        self.get_orders_dict = Orders_repo()
    
    def get_all_cars(self):
        self.cars_dict = self.cars_info.get_cars()
        return self.cars_dict.values()

    def get_available_cars(self):
        self.available_car_list = []
        car_dict = self.cars_info.get_cars()
        today = datetime.date.today()
        for value in car_dict.values():
            old_orders = value.get_orders()
            if old_orders != []:
                for order in old_orders:
                    old_pick_up, old_drop_off = order
                    if (old_pick_up <= today <= old_drop_off): 
                        valid = False
                    else:
                        valid = True

                if valid == True:
                    self.available_car_list.append(value)
            else:
                self.available_car_list.append(value)                          
        return self.available_car_list

    def get_unavailable_cars(self):
        self.unavailable_car_list = []
        car_dict = self.cars_info.get_cars()
        today = datetime.date.today()
        for value in car_dict.values():
            old_orders = value.get_orders()
            if old_orders != []:
                for order in old_orders:
                    old_pick_up, old_drop_off = order
                    if (old_pick_up <= today <= old_drop_off): 
                        valid = True
                    else:
                        valid = False

                if valid == True:
                    self.unavailable_car_list.append(value)
                                        
        return self.unavailable_car_list
    
    def add_car_repo(self, plate_num, brand, size, location ):
        """Adds car to car repo"""
        self.new_car = Car(plate_num, brand, size, location)
        self.cars_info.add_car(plate_num, brand, size, location)

    def get_customer(self, email):
        #nær í customer keys úr dict 
        self.customer_dict = self.customer_info.get_customers()
        #ef keyið passar input frá notanda, returna value úr þeim key
        for key, value in self.customer_dict.items():
            if key == email:
                self.customer = value
                return self.customer
    
    def order_string(self):
        """Returns a string of customer orders"""
        order_string = ""
        orders = self.customer.get_orders()
        for order in orders:
            order_string += "\n" + str(order) + "\n"
        return order_string
            
    def salesman_ID_pw(self,ID, pw):
        """Takes in pw and id from input and checks if it matches the salesman repository"""
        valid = False
        salesman_dict = self.salesman_info.get_salesmen()
        for key, value in salesman_dict.items():
            if key == ID and pw == value.get_password():
                self.salesman_id = key
                self.logged_salesman = value
                valid = True
                return valid
        return valid

    def change_pw(self, new_pw):
        """Id is the key in the salesman dictionary, 
        we use the logged in salesman id to find him in the dictionary and update
        his password by using the change_pw function in the salesman model"""
        salesman_dict = self.salesman_info.get_salesmen()
        for key, value in salesman_dict.items():
            if key == self.salesman_id:
                salesman_object = value
                value.change_pw(new_pw)
                break
        self.salesman_info.update_data(salesman_dict)
        update_repo = self.log_repo
        update_repo.Update_repo("{} changed his password. ID: {}".format(salesman_object.get_name(), \
        salesman_object.get_ID()))

    def get_order_info(self, booking_num):
        order_list = []
        order_dict = self.get_orders_dict.get_orders()
        for values in order_dict.values():
            for order in values:
                if booking_num == order.get_order_num():
                    order_list.append(order)
        return order_list

    def get_log(self):
        return self.log_repo.Read_repo()
    
    def delete_customer(self, customer):
        """Deletes customer if the email input matches the customer database. 
        Then we update the customer repository."""
        cust_dict = self.customer_info.get_customers()
        cust_dict.pop(customer.get_email())
        self.customer_info.add_customers(cust_dict)

        order_dict = self.get_orders_dict.get_orders()
        for plate_num, orders in order_dict.items():
            for order in orders:
                if customer.get_email() == order.get_cust_email():
                    orders.remove(order)

        self.get_orders_dict.update_order_file(order_dict)
    
    def add_to_log(self, ID, brand, plate_num):
        """Updates log when salesman adds a car to the system"""
        update_repo = self.log_repo
        update_repo.Update_repo("{}, ID: {}, Added {} with plate number {} in {}".format(self.logged_salesman.get_name(), \
        ID, brand, plate_num, self.new_car.get_location_string()))

    def delete_customer_to_log(self, ID):
        """Updates log when salesman deletes order"""
        update_repo = self.log_repo
        update_repo.Update_repo("{}, ID: {}, deleted customer {} {}".format(self.logged_salesman.get_name(), \
        ID, self.customer.get_first_name(), self.customer.get_last_name()))

        