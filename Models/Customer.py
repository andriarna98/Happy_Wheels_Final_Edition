#Repos
from Repository.Orders_repo import Orders_repo

class Customer:
    def __init__(self, first_name, last_name, date_of_birth, email, country, address, zip_code, phone, card, security_code, exp_date, orders=[]):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.address = address
        self.zip_code = zip_code
        self.phone = phone 
        self.card = card
        self.security_code = security_code
        self.exp_date = exp_date
        self.orders = orders

    def __repr__(self):
        return repr([self.first_name, self.last_name,self.date_of_birth,
        self.country, self.address, self.zip_code, self.phone])
    
    def __str__(self):
        return "\t\tFirst name: {:10}\tLast name: {:10}\n\t\tEmail: {:10}\tCountry: {:10}" \
    "\n\t\tAddress: {:10}\tZip code: {:10}\n\t\tPhone: {:10}\tCard: {:10}".format(self.first_name, self.last_name, 
            self.email, self.country, self.address, self.zip_code, self.phone, self.card)
    
    def get_first_name(self):
        return self.first_name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_last_name(self):
        return self.last_name
    
    def get_date_of_birth(self):
        return self.date_of_birth
    
    def get_country(self):
        return self.country
    
    def get_address(self):
        return self.address
    
    def get_zip_code(self):
        return self.zip_code

    def get_card_info(self):
        return [self.card, self.security_code, self.exp_date]

    def get_orders(self):
        customer_orders = []
        order_dict = Orders_repo()
        for orders in order_dict.get_orders().values():
            for order in orders:
                if order.get_cust_email() == self.email:
                    customer_orders.append(order)
        return customer_orders

        
    

