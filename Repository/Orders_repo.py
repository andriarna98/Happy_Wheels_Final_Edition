#Models
from Models.Order import Order
#Csv
import csv

class Orders_repo:
    def __init__(self):
        pass
    
    def update_order_file(self, order_dict):
        #first add to file then to private list
        with open("data/Orders.csv", "w+") as Order_file:
            Order_file.write("plate_num,pick_up_date,drop_off_date,order_num,cust_email")
            for plate_num, values in order_dict.items():
                for order in values:
                    pick_up_date = order.get_pick_up_date()
                    drop_off_date = order.get_drop_off_date()
                    cust_email = order.get_cust_email()
                    order_num = order.get_order_num()
                    Order_file.write("\n{},{},{},{},{}".format(plate_num,pick_up_date,drop_off_date,order_num,cust_email))


    def get_orders(self):
        with open("./data/Orders.csv", "r") as Order_file:
            csv_reader = csv.reader(Order_file)
            next(csv_reader)
            self.order_dict = {}
            for line in csv_reader:
                plate_num,pick_up_date,drop_off_date,order_num,cust_email = line
                existing_order = Order(order_num, pick_up_date,drop_off_date,plate_num,cust_email)
                key = existing_order.get_plate_number() 
                if key in self.order_dict.keys():
                    self.order_dict[key].append(existing_order)
                else:
                     self.order_dict[key] = [existing_order]

        return self.order_dict

