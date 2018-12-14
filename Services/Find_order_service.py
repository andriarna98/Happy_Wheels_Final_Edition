#Models
from Models.Order import Order
#Repos
from Repository.Orders_repo import Orders_repo

class Find_order_service:
    def __init__(self):
        #Repos
        self.orders_repo = Orders_repo()

    def delete_order(self, key):
        """Deletes order from the order dictionary and updates the order repository"""
        order_dict = self.orders_repo.get_orders()
        for plate_num, orders in order_dict.items():
            for order in orders:
                if key == order.get_order_num():
                    orders.remove(order)
        self.orders_repo.update_order_file(order_dict)

    def get_order(self, key):
        """Returns the order that matches the order number from the user input"""
        order_dict = self.orders_repo.get_orders()
        for plate_num, orders in order_dict.items():
            for order in orders:
                if key == order.get_order_num():
                    return order
        

                
            

