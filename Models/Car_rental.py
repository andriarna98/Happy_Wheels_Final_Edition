class Car_rental:
    def __init__(self, name, address, phone, email, empl_num, 
    avail_cars_num, unavail_cars_num):
        self.name = name   #Name
        self.address = address  #Address
        self.phone = phone  #phone num
        self.email = email  #email
        self.empl_num = empl_num    # Number of employes working at car rental
        self.avail_cars_num = avail_cars_num    # Num of available cars
        self.unavail_cars_num = unavail_cars_num # Num of unavalable cars

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.name, self.address, self.phone, 
        self.email, self.empl_num, self.avail_cars_num, self.unavail_cars_num)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_empl_num(self):
        return self.empl_num

    def get_avail_cars_num(self):
        return self.avail_cars_num
    
    def get_unavail_cars_num(self):
        return self.unavail_cars_num