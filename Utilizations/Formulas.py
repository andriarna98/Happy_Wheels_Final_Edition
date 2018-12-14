#Datetime
import datetime

class Formulas:
    def __init__(self):
        pass
    
    def calculate_price(self, base_price, date_list, additional_price):
        TAX = 1.24  # Tax put on base price and on the mandatory insurance
        """ Calculates base price of car * days rented """
        pick_up, drop_off = date_list
        days = drop_off - pick_up
        price = int((base_price * days.days * TAX) + additional_price)
        return price