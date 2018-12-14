#Models
from Models.Order import Order
#Repos
from Repository.Orders_repo import Orders_repo

class Car:
    def __init__(self, plate_number, brand, car_size, location, price=0, insurance=0):
        self.car_size = car_size
        self.plate_number = plate_number
        self.brand = brand
        self.location = location
        self.price = price
        self.insurance = insurance
        self.loc_str = ""

    # def __str__(self):
        # return "{},{},{},{}".format(self.plate_number, self.brand, self.car_size, self.get_orders())

    def __repr__(self):
        return repr([self.brand, self.car_size, self.get_orders(), self.location])
        
    def get_plate_number(self):
        return self.plate_number

    def get_car_size(self): # Stærð bíls; small, medium, SUV(large) / Verdflokkur basicly
        return self.car_size

    def get_brand(self):    # Heiti bíls (Frekar name?)
        return self.brand

    def get_pri_ins(self): 
        """ Returns price and cost of insurance of car """
        if self.car_size == "1":
            self.price = 7500
            self.insurance = 2500
        elif self.car_size == "2":
            self.price = 11500
            self.insurance = 3500
        elif self.car_size == "3":
            self.price = 15000
            self.insurance = 4500
        return self.price, self.insurance

    def get_orders(self):
        """Returns list of orders, example list = [[10102018,10122018],[12122018,12142018]], one list represents one order"""
        order_dict = Orders_repo()
        order_list = []
        valid = False
        for key, values in order_dict.get_orders().items():
            if key == self.plate_number: #check if number plate matches a key in the dict
                for order in values:
                    pick_up_date = order.get_pick_up_date()
                    drop_off_date = order.get_drop_off_date()
                    date = [pick_up_date, drop_off_date]
                    order_list.append(date)
                    valid = True     
        if valid == True:
            return order_list
        else:
            return []

    
    def get_location(self):
        return self.location

    def get_location_string(self):
        if self.location == "1":
            self.loc_str = "Reykjavík"
        elif self.location == "2":
            self.loc_str = "Keflavík"
        elif self.location == "3":
            self.loc_str = "Akureyri"
        return self.loc_str

    # def get_year(self):
    #     return self.year

    # def get_doors(self):
    #     return self.doors

    # def get_kilometers(self):
    #     return self.kilometers

    # def get_transmission(self):
    #     return self.transmission
    
    # def get_color(self):
    #     return self.color
    
    # def get_CO2(self):
    #     return self.CO2

    # def get_seats(self):
    #     return self.seats

    # def get_insurance(self):
    #     return self.insurance
    
    # def get_fuel_type(self):
    #     return self.fuel_type
    
    # def get_highlander(self):
    #     return self.highlander